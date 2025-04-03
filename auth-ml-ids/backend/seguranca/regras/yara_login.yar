rule Login_Suspeito
{
    meta:
        description = "Detecta comportamento de login suspeito com base em reputação e horário"
        autor = "auth-ml-ids"
        criacao = "2025-04-02"

    strings:
        $reputacao_ruim = "ip_reputation\": 1"
        $horario_critico_2 = "login_time\": 2"
        $horario_critico_3 = "login_time\": 3"
        $horario_critico_4 = "login_time\": 4"

    condition:
        $reputacao_ruim and any of ($horario_critico_2, $horario_critico_3, $horario_critico_4)
}
