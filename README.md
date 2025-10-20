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


