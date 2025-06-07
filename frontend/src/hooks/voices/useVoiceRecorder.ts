import { useRef, useState } from "react";

/**
 * 音声登録
 */
export function useVoiceRecorder(onStop: (blob: Blob) => void) {
  const [isRecording, setIsRecording] = useState(false);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const audioChunksRef = useRef<Blob[]>([]);

  // 録音開始
  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorderRef.current = mediaRecorder;
    audioChunksRef.current = [];
    setIsRecording(true);

    // データを配列に入れる
    mediaRecorder.ondataavailable = (e) => {
      if (e.data.size > 0) {
        audioChunksRef.current.push(e.data);
      }
    };

    // 録音終わり
    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunksRef.current, { type: "audio/wav" });
      onStop(audioBlob);
      setIsRecording(false);
    };

    mediaRecorder.start();
  };

  // 録音終了
  const stopRecording = () => {
    mediaRecorderRef.current?.stop();
  };

  return {
    isRecording,
    startRecording,
    stopRecording,
  };
}
