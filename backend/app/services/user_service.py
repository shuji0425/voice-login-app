from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app.schemas.user import UserCreate
from app.repositories.user_repository import UserRepository
from app.services.exceptions import UserAlreadyExistsError

# ユーザーサービス
class UserService:
    @staticmethod
    def register(user: UserCreate, db: Session) -> None:
        # 存在チェック
        if UserRepository.exists_by_user_id(user.user_id, db):
            raise UserAlreadyExistsError()

        # パスワードをハッシュ化
        hashed_password = bcrypt.hash(user.password)

        # ユーザー登録
        UserRepository.create_user(user.user_id, hashed_password, db)