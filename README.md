# TrabRecursividade

Cálculo Fatorial Recursivo
R1:
elif a == 0 or a == 1:
       return 1
       #Caso base aqui, pois ele para de chamar a função

R2:
else:
       return a * fatorial(a-1)
       '''
       Aqui chamamos a recursividade, quando o "a" é maior que 1 ou 0 e não é
       negativos é aplicado até chegar ao Caso base.
       '''

R3:
a = 4 entra na funcão quando chamamos ele aqui:

num = 4
print(f"Fatorial de {num} é {fatorial(num)}")
Como a = 4, ele vai direto para o else:
   else:
       return a * fatorial(a-1)
       
Aqui começa a recursividade, a = 3 a partir desse ponto e isso segue até a =1. O que é chamado de Caso base:

   elif a == 0 or a == 1:
       return 1
       
Aqui ao retornar 1 a def para "chamar a si mesma”e com isso possuimos uma saída de:

Fatorial de 4 é 24

Busca Binário Recursiva
R1: É obrigatório o array estar ordenado, porque a lógica por trás do nosso código depende disto, seguimos cortando o array pela metade para ver se ele está em uma metade ou outra, ou seja, somos 100% orientados pela ordem desses números. Se o array não fosse ordenado e primeira coisa que teríamos que fazer era achar uma maneira/função que ordenasse ele.

R2: Nesta etapa “cortamos” ele pela metade: Ao chamar meio(definido anteriormente para ser nosso novo início ou fim.

    elif valor < array[meio]:
        return binarySearch(array,valor,inicio,meio-1)
        
    elif valor > array[meio]:
        return binarySearch(array,valor,meio+1,fim)

R3:Caso base de sucesso é esta etapa: Quando ao cortar encontramos ele

    if valor == array[meio]:
        return f"Valor encontrado = {meio}"
Já o caso base de falha seria esse: para testar se não ocorreu um erro no pedido dos valores:

    if inicio > fim:
        return "Valor não encontrado"
        #Caso base de falha

        
Torres de Hanói Recursiva

R1: O problema consiste em mover N discos de um pino de origem para um pino de destino, utilizando um pino auxiliar, respeitando as regras:

só é possível mover um disco por vez,

e nunca um disco maior pode ficar em cima de um menor.

A função recebe quatro parâmetros:
hanoi(n, origem, destino, auxiliar).

Quando o número de discos n é maior que 1, a função se chama novamente (recursividade) para resolver o mesmo problema, porém com N−1 discos.

R2: A lógica da recursão segue três passos principais, que se repetem até chegar ao caso base:

Mover N−1 discos da origem para o pino auxiliar
→ Aqui a função é chamada novamente:
hanoi(n - 1, origem, auxiliar, destino)
Isso resolve a parte superior da torre (os menores discos) e os coloca no pino auxiliar.

Mover o disco N (o maior) da origem para o destino
→ Este é o movimento direto, exibido no print(f"Mover disco {n} de {origem} para {destino}").

Mover os N−1 discos do auxiliar para o destino
→ A função é chamada mais uma vez:
hanoi(n - 1, auxiliar, destino, origem)
Agora, os discos menores são colocados sobre o disco maior, finalizando o movimento.

Esses três passos são aplicados repetidamente até que reste apenas um disco.

R3 (Caso Base):
O caso base ocorre quando N = 1.
Nesse ponto, a recursão para de se chamar e o movimento é feito diretamente:

if n == 1:
    print(f"Mover disco 1 de {origem} para {destino}")
    return


Esse é o momento em que a função começa a “desenrolar”, retornando os resultados acumulados das chamadas anteriores.
Assim, todos os movimentos são impressos em ordem, simulando a transferência completa dos discos.

