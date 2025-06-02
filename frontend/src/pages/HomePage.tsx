import { useNavigate } from "react-router-dom";

export default function HomePage() {
  const navigate = useNavigate();

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ホーム画面</h1>
      <button
        onClick={() => navigate("/login")}
        className="bg-red-600 text-white px-4 py-2 rounded cursor-pointer"
      >
        ログアウト
      </button>
    </main>
  );
}
