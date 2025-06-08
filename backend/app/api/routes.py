from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.core.db import get_db
from app.handlers import register_handler, login_handler, voice_handler
from app.dependencies.auth import get_current_user_id

router = APIRouter()


# ユーザー登録
@router.post("/api/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_handler.handler_register(user, db)


# ログイン
@router.post("/api/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    return login_handler.handle_login(user, db)


# ログイン済みか確認
@router.get("/api/protected")
def protected_route(user_id: str = Depends(get_current_user_id)):
    return {"message": f"ようこそ、{user_id} さん！"}


# 音声登録
@router.post("/api/voice-register")
def voice_register(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
):
    return voice_handler.handle_voice_register(file, user_id, db)


# 音声ログイン
@router.post("/api/voice-login")
def voice_login(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    return voice_handler.handle_voice_login(file, db)