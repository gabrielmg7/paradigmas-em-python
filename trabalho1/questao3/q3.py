# Desenvolva um Programa em PYTHON usando o comando FOR, 
# para imprimir os números pares de 0 a 100 e a soma destes números.

numero = 0;
soma = 0;

for numero in range(0, 100, 1):
    if numero % 2 == 0:            
        print("Valor: ", numero)
        res = soma + numero
        print("Soma: ", soma, " + ", numero, " = ", res, "\n-----------------------------")
        soma = res
    