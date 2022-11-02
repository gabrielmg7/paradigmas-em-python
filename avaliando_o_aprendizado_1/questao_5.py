def maiorDaLista(lista):
    n = len(lista)
    aux = lista[0]
    ind = 0
    for i in range(lista):
        if aux:
            aux = lista[i]
            ind = i
    return aux


#teste
l = [3, 6, 1, 7, 4]
maior = maiorDaLista(l)
print("maior valor:", maior, ", indice na lista", ind) # o ind tem escopo local e não global
