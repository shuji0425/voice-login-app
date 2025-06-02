import { useNavigate } from "react-router-dom";

/**
 * 登録画面
 */
export default function RegisterPage() {
  const navigate = useNavigate();

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">ユーザー登録</h1>
      <button
        onClick={() => navigate("/home")}
        className="bg-blue-600 text-white px-4 py-2 rounded  cursor-pointer"
      >
        登録してログイン
      </button>
    </main>
  );
}
