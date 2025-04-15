# X e Y
x = int(input())
y = int(input())

# Do menor para o maior
inicio = min(x, y) + 1
fim = max(x, y)

# Calculo + Resultado
for i in range(inicio, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
