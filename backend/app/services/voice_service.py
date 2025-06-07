import os
from resemblyzer import VoiceEncoder, preprocess_wav
from tempfile import NamedTemporaryFile
from fastapi import UploadFile
from sqlalchemy.orm import Session
from app.repositories.voice_repository import create_embedding
from app.repositories.user_repository import UserRepository

encoder = VoiceEncoder()


# 音声登録処理
def register_voice(file: UploadFile, user_id: str, db: Session):
    tmp_path = ""
    try:
        # 一時ファイルを作成
        with NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(file.file.read())
            tmp_path = tmp.name

        # 音声前処理と埋め込み生成
        wav = preprocess_wav(tmp_path)
        embedding = encoder.embed_utterance(wav)

        # user_idをキーにユーザーを取得
        db_user = UserRepository.get_by_user_id(user_id, db)
        int_user_id = db_user.id

        # DBに登録
        create_embedding(db, int_user_id, embedding.tolist())
    finally:
        # 一時ファイルを削除
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
