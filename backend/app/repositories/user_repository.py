from sqlalchemy.orm import Session
from app.models.user import User


# ユーザーレポジトリー
class UserRepository:
    # ユーザー取得
    @staticmethod
    def get_by_user_id(user_id: str, db: Session) -> User | None:
        return db.query(User).filter(User.user_id == user_id).first()

    # ユーザー取得（id)
    @staticmethod
    def get_by_id(id: int, db: Session) -> User | None:
        return db.query(User).filter(User.id == id).first()

    # ユーザーIDの存在チェック
    @staticmethod
    def exists_by_user_id(user_id: str, db: Session) -> bool:
        """同一の user_id が存在するか確認"""
        return db.query(User).filter(User.user_id == user_id).first() is not None

    # ユーザー登録
    @staticmethod
    def create_user(user_id: str, password_hash:str, db:Session) -> User:
        """新しいユーザーを登録"""
        new_user = User(user_id=user_id, password_hash=password_hash)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user