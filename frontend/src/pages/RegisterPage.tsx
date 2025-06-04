import { useState } from "react";
import { useNavigate } from "react-router-dom";

/**
 * 登録画面
 */
export default function RegisterPage() {
  const navigate = useNavigate();
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async () => {
    setError("");

    try {
      const res = await fetch("http://localhost:8000/api/register", {
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
        throw new Error(data.detail || "登録に失敗しました");
      }

      navigate("/home");
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError("予期せぬエラーが発生しました");
      }
    }
  };

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ユーザー登録</h1>
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
        onClick={handleRegister}
        className="bg-blue-600 text-white px-4 py-2 rounded  cursor-pointer"
      >
        登録
      </button>

      <p className="mt-4">
        アカウントのある方は
        <button
          onClick={() => navigate("/login")}
          className="text-blue-500 underline cursor-pointer"
        >
          ログイン
        </button>
      </p>
    </main>
  );
}
