def hanoi(n, origem, destino, auxiliar):
    # Caso base: quando só há 1 disco, move direto
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    # Passo 1: mover N-1 discos da origem para o auxiliar
    hanoi(n - 1, origem, auxiliar, destino)

    # Passo 2: mover o disco restante (maior) da origem para o destino
    print(f"Mover disco {n} de {origem} para {destino}")

    # Passo 3: mover os N-1 discos do auxiliar para o destino
    hanoi(n - 1, auxiliar, destino, origem)


# Exemplo de execução:
n = 3  # número de discos
hanoi(n, 'A', 'C', 'B')