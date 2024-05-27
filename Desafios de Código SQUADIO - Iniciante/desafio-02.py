# Desafio: Lista de itens

# Lista para armazenar os itens
itens = []

# Solicita ao usuário o nome dos três itens, um de cada vez
for i in range(1, 4):
    item = input()
    itens.append(item)

# Exibe a lista de itens cadastrados
print("\nLista de itens:")
for item in itens:
    print(f"- {item}")