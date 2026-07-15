from app.db.database import Base, engine

from app.models.landlord import Landlord
from app.models.user import User

Base.metadata.create_all(bind=engine)