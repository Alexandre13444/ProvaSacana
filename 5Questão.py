# Quantidade Alunos
n = int(input("Digite a quantidade de alunos: "))

# Lista Notas

notas = []
for i in range(n):
    nota = float(input())
    notas.append(nota)

# Calculo Media

media = sum(notas) / n

# Limite de media (superior ou inferior)

limite_superiro = media * 1.10
limite_inferior = media * 0.90

# Contador de notas acima e abaixo da media

acima10 = sum(1 for nota in notas if nota > limite_superiro)
abaixo10 = sum(1 for nota in notas if nota < limite_inferior)

# Resultado

print(f"media: {media:.2f}")
print(f"Notas acima da media: {acima10}")
print(f"Notas abaixo da media: {abaixo10}")
