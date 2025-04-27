from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.user import UserCreate, UserWithToken, UserLogin, UserResponse
from app.cruds import user as user_crud
from app.services.auth import create_access_token, authenticate_user, get_current_user
from app.models.user import User


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/sign-up/", response_model=UserWithToken)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = user_crud.get_user_by_email(db, user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = user_crud.create_user(db, user_data)
    token = create_access_token({"sub": user.email})
    return {"id": user.id, "email": user.email, "token": token}


@router.post("/login/", response_model=UserWithToken)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, user_data.email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not authenticate_user(user, user_data.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    token = create_access_token({"sub": user.email})
    return {"id": user.id, "email": user.email, "token": token}


@router.get("/users/me/", response_model=UserResponse)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get('/')
def hello_print():
    return "Hello, please check /docs !"