import { useState } from "react";
import { useNavigate } from "react-router-dom";

/**
 * ログインページ
 */
export default function LoginPage() {
  const navigate = useNavigate();
  const [userId, setUserId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

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
