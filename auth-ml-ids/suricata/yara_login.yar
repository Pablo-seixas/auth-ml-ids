rule Login_Suspeito
{
    strings:
        $reputacao_ruim = "ip_reputation\": 1"
        $horario_critico = "login_time\": 2"
        $horario_critico2 = "login_time\": 3"
        $horario_critico3 = "login_time\": 4"
    condition:
        any of them
}
