import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { sendVoiceBlob } from "../lib/api/voice/send";
import { useVoiceRecorder } from "../hooks/voices/useVoiceRecorder";

/**
 * ログインページ
 */
export default function LoginPage() {
  const navigate = useNavigate();
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  // ログイン
  const handleLogin = async () => {
    setError("");

    try {
      const res = await fetch("http://localhost:8000/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: userId,
          password: password,
        }),
      });

      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || "ログインに失敗しました");
      }

      // tokenをストレージに保存
      const data = await res.json();
      localStorage.setItem("accessToken", data.access_token);

      navigate("/home");
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("予期せぬエラーが発生しました");
      }
    }
  };

  // 音声ログイン
  const { isRecording, startRecording, stopRecording } = useVoiceRecorder(
    async (blob) => {
      try {
        const data = await sendVoiceBlob(
          "http://localhost:8000/api/voice-login",
          blob
        );
        localStorage.setItem("accessToken", data.access_token);

        navigate("/home");
      } catch {
        setError("音声データの送信に失敗しました。");
      }
    }
  );

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ログイン</h1>
      {error && <p className="text-red-500 mb-2">{error}</p>}

      <input
        type="text"
        className="border rounded w-full p-2 mb-2"
        placeholder="ユーザーID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
      />
      <input
        type="password"
        className="border rounded w-full p-2 mb-4"
        placeholder="パスワード"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button
        onClick={handleLogin}
        className="bg-green-600 text-white px-4 py-2 rounded  cursor-pointer"
      >
        ログインする
      </button>

      {/* 音声登録 */}
      <div className="mt-4">
        <p>{error}</p>
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

      <p className="mt-4">
        アカウントがない方は
        <button
          onClick={() => navigate("/register")}
          className="text-blue-500 underline cursor-pointer"
        >
          登録
        </button>
      </p>
    </main>
  );
}
