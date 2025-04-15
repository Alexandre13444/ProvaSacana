numero = int(input("Insira o numero: "))

# Menor que 2

if numero < 2:
    print("Não é primo")
else:
    # Verificar se é primo
    SimPrimo = True
    for i in range(2, int(numero ** 0.5)+1):
        if numero % i == 0:
            SimPrimo = False
            break

# Resultado

if SimPrimo:
    print("É um número primo")
else:
    print("Não é um número primo")
