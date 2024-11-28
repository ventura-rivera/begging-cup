from begging_cup.models.user import User
from begging_cup.schemas.user import UserCreate
from sqlalchemy.orm import Session


def create_user(db: Session, user_create: UserCreate):
    user = User(**user_create.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user