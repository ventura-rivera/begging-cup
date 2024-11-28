from fastapi import FastAPI, Request, Form, Depends
from begging_cup.core.templates import templates
from begging_cup.utils import crud, security
from begging_cup.schemas.user import UserCreate
from begging_cup.core.database import get_db, Base, engine
from sqlalchemy.orm import Session



Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def home(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("subscribe.html", context)

@app.get("/create-user")
async def create_user_form(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("create-user.html", context)

@app.post("/users")
async def create_user(
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    hashed_password = security.hash_password(password=password)
    user_create = UserCreate(email=email, hashed_password=hashed_password)
    user = crud.create_user(db=db, user_create=user_create)
    return user