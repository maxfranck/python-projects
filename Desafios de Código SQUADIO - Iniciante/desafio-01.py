# Desafio: A Aventura do Explorador
      
# Entrada
quantidade_passos = int(input())

if quantidade_passos >= 0:
    if quantidade_passos == 0:
        print("Nenhum passo dado na floresta.")
    else:
        for passo in range(quantidade_passos):
            if passo == 0:
                print(f"Explorador: {passo + 1} passo")
            else:
                print(f"Explorador: {passo + 1} passos")
