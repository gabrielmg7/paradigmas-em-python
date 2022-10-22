def soma(x, y):
    print("Somando...")
    return x + y


def subtracao(x, y):
    print("Subtraindo...")
    return x - y


def multiplicacao(x, y):
    print("Multiplicando...")
    return x * y


def divisao(x, y):
    print("Dividindo...")
    return x / y


def main(res):
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("--------------------")
    op = int(input("Operação desejada: "))
    print("--------------------")
    if op == 1:
        print("Resultado: ", soma(x, y))
    elif op == 2:
        print("Resultado: ", subtracao(x, y))
    elif op == 3:
        print("Resultado: ", multiplicacao(x, y))
    elif op == 4:
        print("Resultado: ", divisao(x, y))
    elif op != (1 or 2 or 3 or 4):
        print("Opção inválida! Escolha de 1 a 4.")
        print("Retornando para Main...")
        main(res)

    print("--------------------")

res = 0
main(res)
