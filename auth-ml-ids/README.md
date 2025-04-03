Backend - FastAPI

 Backend - FastAPI
O backend foi construído com FastAPI e tem como objetivo:

Receber tentativas de login via POST

Prever possíveis fraudes usando um modelo de machine learning (modelo_ml.pkl)

Registrar logs de acessos no banco SQLite (users.db)

Expor uma interface interativa via Swagger em /docs



 Estrutura

backend/
├── app.py                # API principal com rotas
├── utils.py              # [em breve] Funções auxiliares
├── modelo_ml.pkl         # Modelo de ML fake para predição
├── train_fake_model.py   # Script para gerar o modelo fake


Rotas implementadas
 GET /
Verifica se a API está online
Resposta:

json

{ "status": "API de Autenticação Segura Ativa" }


POST /login
Recebe um JSON com o usuário

Gera predição com modelo ML

Salva no banco



Exemplo de chamada:

curl -X POST http://127.0.0.1:8000/login \
 -H "Content-Type: application/json" \
 -d '{"user": "admin"}'



Resposta:

json
Copiar
Editar
{
  "user": "admin",
  "ip": "127.0.0.1",
  "status": "normal"
}



Banco de Dados
O banco users.db é criado via script:

 scripts/setup_env.sh

Ele contém a tabela:

sql

CREATE TABLE logs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT,
  ip TEXT,
  timestamp TEXT,
  status TEXT
);




Modelo de Machine Learning (Fake)
Foi gerado um modelo fake com RandomForestClassifier que sempre retorna "normal" para testes iniciais.

python3 backend/train_fake_model.py
Arquivo salvo como: backend/modelo_ml.pkl


