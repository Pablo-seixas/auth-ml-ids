#!/bin/bash

echo "[+] Criando banco SQLite..."
mkdir -p db
sqlite3 db/users.db <<EOF
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    ip TEXT,
    timestamp TEXT,
    status TEXT
);
EOF

echo "[+] Banco criado com sucesso em db/users.db"
