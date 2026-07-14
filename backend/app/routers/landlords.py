from fastapi import APIRouter

router = APIRouter(
    prefix="/landlords",
    tags=["Landlords"]
)

# Temporary in-memory storage
landlords = []

@router.get("/")
def get_landlords():
    return landlords

@router.post("/")
def add_landlord(landlord: dict):
    landlord["id"] = len(landlords) + 1
    landlords.append(landlord)
    return {
        "message": "Landlord added successfully",
        "data": landlord
    }
