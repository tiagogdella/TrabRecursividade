def fatorial (a):
    if a < 0:
        return "error"
    elif a == 0 or a == 1:
        return 1
        #Caso base aqui, pois ele para de chamar a função
    else:
        return a * fatorial(a-1)
        '''
        Aqui chamamos a recursividade, quando o "a" é maior que 1 ou 0 e não é 
        negativos é aplicado até chegar ao Caso base.
        '''

num = 4
print(f"Fatorial de {num} é {fatorial(num)}")