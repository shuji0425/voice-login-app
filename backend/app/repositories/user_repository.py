from sqlalchemy.orm import Session
from app.models.user import User


# ユーザーレポジトリー
class UserRepository:
    @staticmethod
    def exists_by_user_id(user_id: str, db: Session) -> bool:
        """同一の user_id が存在するか確認"""
        return db.query(User).filter(User.user_id == user_id).first() is not None

    @staticmethod
    def create_user(user_id: str, password_hash:str, db:Session) -> User:
        """新しいユーザーを登録"""
        new_user = User(user_id=user_id, password_hash=password_hash)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user