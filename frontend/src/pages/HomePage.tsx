import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

/**
 * ホーム
 */
export default function HomePage() {
  const navigate = useNavigate();
  const [message, setMessage] = useState("");

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

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ホーム画面</h1>
      <p>{message}</p>
      <button
        onClick={handleLogout}
        className="bg-red-600 text-white mt-4 px-4 py-2 rounded cursor-pointer"
      >
        ログアウト
      </button>
    </main>
  );
}
