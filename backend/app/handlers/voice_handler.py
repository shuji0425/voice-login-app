from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.services.voice_service import VoiceEmbeddingService


# 音声ログイン
def handle_voice_login(file: UploadFile, db: Session):
    return VoiceEmbeddingService.login_with_voice(file, db)

# 音声登録
def handle_voice_register(file: UploadFile, user_id: str, db: Session):
    VoiceEmbeddingService.register_voice(file, user_id, db)
    return {"message": "音声を登録しました"}
