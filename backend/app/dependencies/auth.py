from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.jwt import get_user_id_from_token

# 認証トークン用のスキーマ
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

# ログイン判定
def get_current_user_id(token: str = Depends(oauth2_scheme)) -> str:
    try:
        return get_user_id_from_token(token)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="認証エラー：トークンが無効です"
        )