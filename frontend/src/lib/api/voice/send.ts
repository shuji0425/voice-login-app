/**
 * 音声データ送信
 * @param endpoint エンドポイント(URL)
 * @param blob     音声データ
 * @returns json
 */
export async function sendVoiceBlob(endpoint: string, blob: Blob) {
  const token = localStorage.getItem("accessToken");
  const formData = new FormData();
  formData.append("file", blob, "voice.wav");

  const res = await fetch(endpoint, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
    },
    body: formData,
  });

  if (!res.ok) throw new Error("送信失敗");
  return await res.json();
}
