from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from app.services.exceptions import UserAlreadyExistsError

def handler_register(user: UserCreate, db: Session):
    try:
        UserService.register(user, db)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=400, detail="同じIDを使っている人がいるので辞めてください")
    return {"message": "User registered successfully"}