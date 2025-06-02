import { useNavigate } from "react-router-dom";

/**
 * ログインページ
 */
export default function LoginPage() {
  const navigate = useNavigate();

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ログイン</h1>
      <button
        onClick={() => navigate("/home")}
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
