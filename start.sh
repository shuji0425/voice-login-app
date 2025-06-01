#!/bin/bash

# フロントエンドの起動（バックグラウンド）
cd frontend
npm run dev > ../frontend.log 2>&1 &
FRONT_PID=$!

# バックエンドの起動（仮想環境の有効化 → uvicorn起動）
cd ../backend
source venv/bin/activate
uvicorn app.main:app --reload > ../backend.log 2>&1 &
BACK_PID=$!

# 停止時の処理を定義（Ctrl+C や VSCode終了時に両方kill）
cleanup() {
  echo "Stopping processes..."
  kill $FRONT_PID
  kill $BACK_PID
  deactivate
  exit 0
}

# シグナル（終了要求）を受け取ったら cleanup を呼ぶ
trap cleanup INT TERM

# フォアグラウンドで無限ループ（プロセスを維持）
while true; do sleep 1; done
