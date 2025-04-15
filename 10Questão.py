# Quantidade de numeros
n = int(input())

# Lista de numeros
numeros = []
for _ in range(n):
    num = int(input())
    numeros.append(num)

# A) Ordem Inversa
print("Ordem inversa:")
for num in reversed(numeros):
    print(num)

# b) Ordem Decrescente
print("Ordem decrescente:")
for num in sorted(numeros, reverse=True):
    print(num)
