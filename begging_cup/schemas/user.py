from pydantic import BaseModel


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    hashed_password: str

class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True