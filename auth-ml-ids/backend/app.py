# backend/app.py

from backend.utils import get_client_ip, log_event, get_db_connection
from fastapi import FastAPI, Request
import joblib
import os
from datetime import datetime


from backend.utils import get_client_ip, log_event


app = FastAPI()

# Tenta carregar o modelo ML se existir
MODEL_PATH = "backend/modelo_ml.pkl"
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

#@app.get("/")
def read_root():
    return {"status": "API de Autenticação Segura Ativa"}

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    username = data.get("user", "desconhecido")
    ip_address = request.client.host
    timestamp = datetime.now().isoformat()

    # Placeholder de predição
    prediction = "normal"
    if model:
        try:
            prediction = model.predict([[0, 0, 0]])[0]  # exemplo fixo
        except:
            prediction = "erro_modelo"

    # Grava no banco
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO logs (username, ip, timestamp, status) VALUES (?, ?, ?, ?)",
        (username, ip_address, timestamp, prediction)
    )
    conn.commit()
    conn.close()

    return {
        "user": username,
        "ip": ip_address,
        "status": prediction
    }

@app.get("/logs")
def get_logs():
    conn = get_db_connection()
    logs = conn.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 20").fetchall()
    conn.close()


    return [
        {
            "id": row["id"],
            "username": row["username"],
            "ip": row["ip"],
            "timestamp": row["timestamp"],
            "status": row["status"]
        }
        for row in logs
    ]
