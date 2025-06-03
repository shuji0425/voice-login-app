from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.core.db import get_db
from app.handlers import register_handler

router = APIRouter()

@router.post("/api/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_handler.handler_register(user, db)