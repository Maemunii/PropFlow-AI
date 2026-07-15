from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.landlord import LandlordCreate, LandlordResponse
from app.crud import landlord as crud

from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/landlords",
    tags=["Landlords"],
)

@router.get("/", response_model=list[LandlordResponse])
def get_landlords(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return crud.get_landlords(db)


@router.get("/{landlord_id}", response_model=LandlordResponse)
def get_landlord(
    landlord_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    landlord = crud.get_landlord(db, landlord_id)

    if landlord is None:
        raise HTTPException(status_code=404, detail="Landlord not found")

    return landlord


@router.post("/", response_model=LandlordResponse)
def create_landlord(
    landlord: LandlordCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return crud.create_landlord(db, landlord)


@router.delete("/{landlord_id}")
def delete_landlord(
    landlord_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    landlord = crud.delete_landlord(db, landlord_id)

    if landlord is None:
        raise HTTPException(status_code=404, detail="Landlord not found")

    return {"message": "Landlord deleted successfully"}