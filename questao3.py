def letra_a(numero):
    return numero + 2

def letra_b(numero):
    return numero * 2

def letra_c(numero):
    return (int(numero ** 0.5) + 1) ** 2

def letra_d(numero):
    return (int(numero ** 0.5) + 2) ** 2

def letra_e(numero1, numero2):
    return numero1 + numero2

def letra_f(numero):
    if numero % 2 == 0:
        return numero + 2
    else:
        return numero + 1

# Testando os próximos elementos
print(letra_a(7))  # Saída: 9
print(letra_b(64))  # Saída: 128
print(letra_c(36))  # Saída: 49
print(letra_d(64))  # Saída: 100
print(letra_e(8, 13))  # Saída: 21
print(letra_f(19))  # Saída: 20
