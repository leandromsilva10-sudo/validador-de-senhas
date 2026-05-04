import time

def monitorar_servidor():
    limite_temperatura = 80
    sistema_ativo = True

    print(f"--- Monitoramento Iniciado (Limite: {limite_temperatura}°C) ---")

    try:
        while sistema_ativo:
            # Simulação de entrada do sensor (pode ser substituído por leitura de hardware)
            entrada = input("\nDigite a temperatura atual (ou 'off' para desligar): ")

            if entrada.lower() == 'off':
                sistema_ativo = False
                print("Encerrando monitoramento...")
                break

            try:
                temperatura_atual = float(entrada)

                if temperatura_atual > limite_temperatura:
                    print(f"⚠️ ALERTA: {temperatura_atual}°C! Resfriamento ativado.")
                else:
                    print(f"✅ Temperatura estável: {temperatura_atual}°C.")

            except ValueError:
                print("Erro: Por favor, insira um valor numérico válido.")
            
            # Pequena pausa para não sobrecarregar o processamento
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuário.")

monitorar_servidor()
