from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.core.db import Base

# ユーザーテーブル
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
