from sqlalchemy.orm import Session
from app.models.voice_embedding import VoiceEmbedding

# ユーザーレポジトリー
class VoiceEmbeddingRepository:
    # 全件取得
    @staticmethod
    def get_all_embeddings(db: Session):
        return db.query(VoiceEmbedding).all()

    # 音声登録（user_id = ユーザーDBのidを入れる）
    @staticmethod
    def create_embedding(db: Session, user_id: int, embedding: list[float]):
        voice_embedding = VoiceEmbedding(user_id=user_id, embedding=embedding)
        db.add(voice_embedding)
        db.commit()
