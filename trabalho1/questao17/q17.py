vetor = []

while(len(vetor) < 10):
    num = int(input("Insira um número: "))
    vetor.append(num)

novoVetor = [num for num in reversed(vetor)]
print("Resultado invertido: ", novoVetor)