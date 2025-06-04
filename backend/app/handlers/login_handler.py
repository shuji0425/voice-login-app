from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from app.services.exceptions import UserNotFoundError, InvalidPasswordError

# ログイン
def handle_login(user: UserCreate, db: Session):
    try:
        token = UserService.login(user, db)
    except UserNotFoundError:
        raise HTTPException(status_code=404, detail="ユーザーが見つかりません")
    except InvalidPasswordError:
        raise HTTPException(status_code=401, detail="パスワードが正しくありません")

    return {"access_token": token, "token_type": "bearer"}