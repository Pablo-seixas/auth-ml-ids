#!/bin/bash

echo "[+] Verificando vulnerabilidades com Bandit..."
bandit -r ../../ > backend/seguranca/build/relatorio_bandit.txt
echo "[+] Relatório salvo em backend/seguranca/build/relatorio_bandit.txt"
