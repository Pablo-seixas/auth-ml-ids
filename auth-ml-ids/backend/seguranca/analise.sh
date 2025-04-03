#!/bin/bash

# Atualiza logs da segurança do projeto

# Coletar alertas Suricata
sudo tail -n 200 /var/log/suricata/eve.json | jq 'select(.alert)' > logs/suricata_alertas.json

# Capturar possíveis SYN scans com tshark
sudo tshark -i eth0 -c 100 -Y "tcp.flags.syn == 1 and tcp.flags.ack == 0" -T fields -e frame.time -e ip.src -e ip.dst -e tcp.flags > logs/tshark_synscan.log

# Rodar regra YARA
yara regras/yara_login.yar /var/log/suricata/eve.json > logs/yara_resultados.txt

echo -e "
[✓] Análises completas. Logs salvos em ./logs/"
