from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session
from app.services.voice_service import VoiceEmbeddingService


# 音声ログイン
def handle_voice_login(file: UploadFile, db: Session):
    try:
        token = VoiceEmbeddingService.login_with_voice(file, db)
    except HTTPException as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="サーバーエラーが発生しました")

    return {"access_token": token, "token_type": "bearer"}

# 音声登録
def handle_voice_register(file: UploadFile, user_id: str, db: Session):
    VoiceEmbeddingService.register_voice(file, user_id, db)
    return {"message": "音声を登録しました"}
