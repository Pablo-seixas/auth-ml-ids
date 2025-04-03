import sqlite3
from datetime import datetime



# Conexão com banco
def get_db_connection():
    conn = sqlite3.connect("db/users.db")
    conn.row_factory = sqlite3.Row
    return conn

# Extrai IP real do request
def get_client_ip(request):
    return request.client.host

# Insere log de evento no banco
def log_event(username, ip, status):
    timestamp = datetime.now().isoformat()
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO logs (username, ip, timestamp, status) VALUES (?, ?, ?, ?)",
        (username, ip, timestamp, status)
    )
    conn.commit()
    conn.close()
