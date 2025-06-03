from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 本番では制限すること
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ルート
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Voice Login API is running."}