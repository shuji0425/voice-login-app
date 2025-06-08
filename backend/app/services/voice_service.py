from fastapi import UploadFile
from scipy.spatial.distance import cosine
from sqlalchemy.orm import Session
from app.repositories.voice_repository import VoiceEmbeddingRepository
from app.repositories.user_repository import UserRepository
from app.utils.voice import VoiceUtils
from app.services.exceptions import UserNotFoundError
from app.core.jwt import create_access_token
from datetime import timedelta


class VoiceEmbeddingService:
    # 音声ログイン
    @staticmethod
    def login_with_voice(file: UploadFile, db: Session) -> str:
        tmp_path = ""
        try:
            # 一時ファイルを作成
            tmp_path = VoiceUtils.save_temp_wav(file)
            # 音声前処理と埋め込み生成
            embedding = VoiceUtils.extract_embedding_from_path(tmp_path)

            # 全音声情報を取得
            db_embeddings = VoiceEmbeddingRepository.get_all_embeddings(db)
            if not db_embeddings:
                raise ValueError("登録された音声がありません")
            # 最も近いユーザーを探す
            matched_user_id = None
            best_similarity = -1

            for item in db_embeddings:
                stored = item.embedding
                similarity = 1 - cosine(embedding, stored)
                if similarity > best_similarity:
                    best_similarity = similarity
                    matched_user_id = item.user_id # ユーザーDBのid

            # 閾値でログイン判定（類似度0.71）
            if best_similarity >= 0.71:
                user = UserRepository.get_by_id(matched_user_id, db)
                if not user:
                    raise UserNotFoundError()
                token = create_access_token(
                    data={"sub": user.user_id},
                    expires_delta=timedelta(minutes=30)
                )

                return token
            else:
                raise ValueError("声の一致が見つかりませんでした")
        except Exception as e:
            raise e
        finally:
            # 一時ファイルを削除
            VoiceUtils.delete_temp_file_from_path(tmp_path)


    # 音声登録処理
    @staticmethod
    def register_voice(file: UploadFile, user_id: str, db: Session):
        tmp_path = ""
        try:
            # 一時ファイルを作成
            tmp_path = VoiceUtils.save_temp_wav(file)

            # 音声前処理と埋め込み生成
            embedding = VoiceUtils.extract_embedding_from_path(tmp_path)

            # user_idをキーにユーザーを取得
            db_user = UserRepository.get_by_user_id(user_id, db)
            int_user_id = db_user.id

            # DBに登録
            VoiceEmbeddingRepository.create_embedding(db, int_user_id, embedding)
        finally:
            # 一時ファイルを削除
            VoiceUtils.delete_temp_file_from_path(tmp_path)
