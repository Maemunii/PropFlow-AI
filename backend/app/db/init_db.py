from app.db.database import Base, engine

from app.models.landlord import Landlord

Base.metadata.create_all(bind=engine)

print("Database created.")