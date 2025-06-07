from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.services.voice_service import register_voice


# 音声登録
def handle_voice_register(file: UploadFile, user_id: str, db: Session):
    register_voice(file, user_id, db)
    return {"message": "音声を登録しました"}
