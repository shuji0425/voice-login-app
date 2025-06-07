from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, ARRAY
from sqlalchemy.sql import func
from app.core.db import Base

# 声データテーブル
class VoiceEmbedding(Base):
    __tablename__ = "voice_embeddings"

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    embedding = Column(ARRAY(Float), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
