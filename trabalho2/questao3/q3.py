nome_out = []
idade_out = []
lista = 0


def inserir(nome_out, idade_out, lista):
    while lista < 5:
        nome_out.append(input("Insira o nome: "))
        idade_out.append(input("Insira a idade: "))
        lista = lista + 1
        print("--------------------------")
        print("Nomes: ", nome_out)
        print("Idades: ", idade_out)
        print("--------------------------")
    menu(nome_out, idade_out, lista)


def remover(nome_out, idade_out, lista):
    op = int(input("Qual a posição que você deseja remover? (0-4): "))
    nome_out.pop(op)
    idade_out.pop(op)
    print("--------------------------")
    print("Nomes: ", nome_out)
    print("Idades: ", idade_out)
    print("--------------------------")

    lista = lista - 1

    menu(nome_out, idade_out, lista)


def menu(nome_out, idade_out, lista):
    print("--------------------------")
    print("1- INSERIR PESSOA")
    print("2- REMOVER PESSOA")
    print("0- SAIR")
    print("--------------------------")
    op = int(input("Opção desejada: "))
    if op == 1:
        if (lista == 5):
            print("Lista cheia! Remova um para inserir!")
            print("--------------------------")
            menu(nome_out, idade_out, lista)
        else:
            inserir(nome_out, idade_out, lista)
    elif op == 2:
        remover(nome_out, idade_out, lista)
    elif op == 0:
        SystemExit
    elif op != 1 or 2:
        print("Opção inválida! Retornando...")
        print("--------------------------")


menu(nome_out, idade_out, lista)