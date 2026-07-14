from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Landlord(Base):
    __tablename__ = "landlords"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)

    phone = Column(String)
    whatsapp = Column(String)

    email = Column(String)

    suburb = Column(String)

    notes = Column(String)