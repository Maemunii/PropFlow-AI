from sqlalchemy.orm import Session

from app.models.landlord import Landlord
from app.schemas.landlord import LandlordCreate


def get_landlords(db: Session):
    return db.query(Landlord).all()


def get_landlord(db: Session, landlord_id: int):
    return db.query(Landlord).filter(Landlord.id == landlord_id).first()


def create_landlord(db: Session, landlord: LandlordCreate):
    db_landlord = Landlord(**landlord.model_dump())

    db.add(db_landlord)
    db.commit()
    db.refresh(db_landlord)

    return db_landlord


def delete_landlord(db: Session, landlord_id: int):
    landlord = get_landlord(db, landlord_id)

    if landlord:
        db.delete(landlord)
        db.commit()

    return landlord