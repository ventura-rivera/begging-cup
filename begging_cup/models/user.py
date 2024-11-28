from sqlalchemy import Column, Boolean, String
from begging_cup.core.database import Base

import uuid


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    email_confirmed = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"