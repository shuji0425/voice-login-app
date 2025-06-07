import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useVoiceRecorder } from "../hooks/voices/useVoiceRecorder";
import { sendVoiceBlob } from "../lib/api/voice/send";

/**
 * ホーム
 */
export default function HomePage() {
  const navigate = useNavigate();
  const [message, setMessage] = useState("");
  const [voiceMessage, setVoiceMessage] = useState("");

  // ログインの検証
  useEffect(() => {
    const fetchProtected = async () => {
      const token = localStorage.getItem("accessToken");
      if (!token) {
        navigate("/login");
        return;
      }

      try {
        const res = await fetch("http://localhost:8000/api/protected", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (!res.ok) throw new Error("未認証");

        const data = await res.json();
        setMessage(data.message);
      } catch {
        navigate("/login");
      }
    };

    fetchProtected();
  }, [navigate]);

  // ログアウト処理
  const handleLogout = () => {
    localStorage.removeItem("accessToken");
    navigate("/login");
  };

  const { isRecording, startRecording, stopRecording } = useVoiceRecorder(
    async (blob) => {
      try {
        const data = await sendVoiceBlob(
          "http://localhost:8000/api/voice-register",
          blob
        );
        setVoiceMessage(data.message);
      } catch {
        setVoiceMessage("音声データの送信に失敗しました。");
      }
    }
  );

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ホーム画面</h1>
      <p>{message}</p>

      {/* 音声登録 */}
      <div className="mt-4">
        <p>{voiceMessage}</p>
        {isRecording ? (
          <button
            className="bg-red-600 text-white px-4 py-2 rounded cursor-pointer"
            onClick={stopRecording}
          >
            録音停止
          </button>
        ) : (
          <button
            className="bg-blue-600 text-white px-4 py-2 rounded cursor-pointer"
            onClick={startRecording}
          >
            録音開始
          </button>
        )}
      </div>

      {/* ログアウトボタン */}
      <div>
        <button
          onClick={handleLogout}
          className="bg-red-600 text-white mt-4 px-4 py-2 rounded cursor-pointer"
        >
          ログアウト
        </button>
      </div>
    </main>
  );
}
