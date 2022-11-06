def fatorial(x):
    if x < 0:
        print("Fatorial de um negativo não existe!")

    elif x == 0:
        return 1

    else:
        res = 1
        while (x > 1):
            res *= x
            x -= 1
        return res


x = int(input("Insira um número: "))
print("Fatorial de", x, "é", fatorial(x))
