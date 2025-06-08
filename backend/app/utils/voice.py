import os
from tempfile import NamedTemporaryFile
from fastapi import UploadFile
from resemblyzer import VoiceEncoder, preprocess_wav

encoder = VoiceEncoder()

class VoiceUtils:
    # 一時ファイルに保存してパスを返す
    @staticmethod
    def save_temp_wav(file: UploadFile) -> str:
        with NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(file.file.read())
            return tmp.name

    # wavパスからベクトルを生成
    @staticmethod
    def extract_embedding_from_path(path: str) -> list[float]:
        wav = preprocess_wav(path)
        return encoder.embed_utterance(wav).tolist()

    # 一時ファイルを削除
    @staticmethod
    def delete_temp_file_from_path(path: str) -> None:
        if path and os.path.exists(path):
            os.remove(path)