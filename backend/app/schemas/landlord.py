from pydantic import BaseModel


class LandlordCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str | None = None
    whatsapp: str | None = None
    email: str | None = None
    suburb: str | None = None
    notes: str | None = None


class LandlordResponse(LandlordCreate):
    id: int

    class Config:
        from_attributes = True