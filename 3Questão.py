# Pergunta
Nome = input("Digite seu nome: ")

# Mensagem + Verificação

if len(Nome) <= 120:
    print(f"Seja muito bem-vindo: {Nome}")
else:
    print("Nome grande demais, insira outro por favor")
