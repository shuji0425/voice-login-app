from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.core.db import get_db
from app.handlers import register_handler, login_handler
from app.dependencies.auth import get_current_user_id

router = APIRouter()

@router.post("/api/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_handler.handler_register(user, db)

@router.post("/api/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    return login_handler.handle_login(user, db)

@router.get("/api/protected")
def protected_route(user_id: str = Depends(get_current_user_id)):
    return {"message": f"ようこそ、{user_id} さん！"}