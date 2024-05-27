# Desafio: Armazenamento de Dados é Vida!

capacidade_atual, aumento_percentual = map(int, input().split())

nova_capacidade = int(capacidade_atual + (capacidade_atual * (aumento_percentual / 100)))

print(nova_capacidade)