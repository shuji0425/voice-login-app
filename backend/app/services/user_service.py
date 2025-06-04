from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepository
from app.services.exceptions import UserAlreadyExistsError, UserNotFoundError, InvalidPasswordError
from app.core.jwt import create_access_token
from datetime import timedelta

# ユーザーサービス
class UserService:
    # ユーザー登録
    @staticmethod
    def register(user: UserCreate, db: Session) -> None:
        # 存在チェック
        if UserRepository.exists_by_user_id(user.user_id, db):
            raise UserAlreadyExistsError()

        # パスワードをハッシュ化
        hashed_password = bcrypt.hash(user.password)

        # ユーザー登録
        UserRepository.create_user(user.user_id, hashed_password, db)

    # ログイン
    @staticmethod
    def login(user: UserCreate, db: Session) -> str:
        # ユーザーを検索
        db_user = UserRepository.get_by_user_id(user.user_id, db)
        if not db_user:
            raise UserNotFoundError()

        # パスワード照合
        if not bcrypt.verify(user.password, db_user.password_hash):
            raise InvalidPasswordError()

        token = create_access_token(
            data={"sub": user.user_id},
            expires_delta=timedelta(minutes=30)
        )

        return token