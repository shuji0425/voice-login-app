from sqlalchemy.orm import Session
from app.models.voice_embedding import VoiceEmbedding


# 音声登録（user_id = ユーザーDBのidを入れる）
def create_embedding(db: Session, user_id: int, embedding: list[float]):
    voice_embedding = VoiceEmbedding(user_id=user_id, embedding=embedding)
    db.add(voice_embedding)
    db.commit()
