def fibonacci(numero):
    a, b = 0, 1

    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b

    return False

# Número a ser verificado
numero_informado = 21  # Pode ser alterado para qualquer número desejado

if fibonacci(numero_informado):
    print(f'O número {numero_informado} pertence à sequência de Fibonacci.')
else:
    print(f'O número {numero_informado} não pertence à sequência de Fibonacci.')