def descobrir_interruptores_lampadas():
    print("1. Ligue o interruptor 1 e espere alguns minutos.")
    input("Pressione Enter quando estiver pronto para continuar...")

    print("2. Desligue o interruptor 1 e ligue o interruptor 2.")
    input("Pressione Enter quando estiver pronto para continuar...")

    print("3. Entre na sala das lâmpadas e observe:")
    estado_interruptor_1 = input("Interruptor 1 (Ligado/Desligado): ").lower()
    estado_interruptor_2 = input("Interruptor 2 (Ligado/Desligado): ").lower()
    estado_interruptor_3 = input("Interruptor 3 (Ligado/Desligado): ").lower()

    if estado_interruptor_1 == 'ligado':
        print("A lâmpada 1 está conectada ao interruptor 1.")
    elif estado_interruptor_2 == 'ligado':
        print("A lâmpada 1 está conectada ao interruptor 2.")
    else:
        print("A lâmpada 1 está conectada ao interruptor 3.")

    if estado_interruptor_2 == 'ligado':
        print("A lâmpada 2 está conectada ao interruptor 2.")
    elif estado_interruptor_1 == 'ligado':
        print("A lâmpada 2 está conectada ao interruptor 1.")
    else:
        print("A lâmpada 2 está conectada ao interruptor 3.")

    if estado_interruptor_3 == 'ligado':
        print("A lâmpada 3 está conectada ao interruptor 3.")
    elif estado_interruptor_1 == 'ligado':
        print("A lâmpada 3 está conectada ao interruptor 1.")
    else:
        print("A lâmpada 3 está conectada ao interruptor 2.")

# Executar a função para descobrir a conexão dos interruptores com as lâmpadas
descobrir_interruptores_lampadas()
