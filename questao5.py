def inverter_string(original):
    # Inicializa uma string vazia para armazenar o resultado invertido
    invertida = ""

    # Percorre a string original de trás para frente e adiciona os caracteres à string invertida
    for i in range(len(original) - 1, -1, -1):
        invertida += original[i]

    return invertida

# Exemplo de uso
entrada = input("Digite uma string: ")
resultado = inverter_string(entrada)

print("String original:", entrada)
print("String invertida:", resultado)