def binarySearch(array,valor,inicio,fim):
    if inicio > fim:
        return "Valor não encontrado"
        #Caso base de falha
    
    meio = (inicio+fim)//2

    if valor == array[meio]:
        return f"Valor encontrado = {meio}"
    #Caso base de sucesso
    
    elif valor < array[meio]:
        return binarySearch(array,valor,inicio,meio-1)

    elif valor > array[meio]:
        return binarySearch(array,valor,meio+1,fim)

array = [0,1,2,3,4]
valor = 2
inicio = 0
fim = len(array)-1

print(binarySearch(array,valor,inicio,fim))
