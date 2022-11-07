argumentos = []
x = 0.0
res = 0.0

def soma_args_kwargs(*args):
    for x in args:
        x = float(input("Insira um argumento: "))
        argumentos.append(x)  # insere na lista
        print(x, "inserido!")
        res += x  # incrementa o valor

    if (len(argumentos) == 9):
        print("======================")
        print("Elementos:", argumentos)
        print("Soma de todos:", res)
        print("======================")

while (i < 9):
    soma_args_kwargs(0)
    i += 1

