resultado = 0

numero = int(input("Insira um número: "))

for i in range(1, numero + 1, 1):
    resultado += i
print("Resultado = ", resultado)