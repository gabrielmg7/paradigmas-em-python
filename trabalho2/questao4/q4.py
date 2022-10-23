import os

clear = lambda: os.system('cls')

modelo = []
consumo = []
lista = 0


def inserir_carro(modelo, consumo, lista, clear):
    clear()
    while lista < 5:
        if lista > 0:
            clear()
            print("-----------------------------")
            print("Modelo: ", modelo)
            print("Consumo: ", consumo)
            print("-----------------------------")
        modelo.append(input("Insira o Modelo do carro: "))
        consumo.append(input("Insira quantos Km/litro: "))
        lista = lista + 1

        if (lista == 5):
            clear()
            print("-----------------------------")
            print("Lista cheia!!")
            print("-----------------------------")
            print("Modelo: ", modelo)
            print("Consumo: ", consumo)
    menu(modelo, consumo, lista, clear)


def remover_carro(modelo, consumo, lista, clear):
    clear()
    op = int(input("Qual carro deseja remover? (0-4:) "))
    if op != (0 - 4):
        print("Opção inválida! Retornando...")
        menu(modelo, consumo, lista, clear)
    else:
        modelo.remove(op)
        consumo.remove(op)
    print("-----------------------------")
    print("Modelo: ", modelo)
    print("Consumo: ", consumo)
    print("-----------------------------")
    menu(modelo, consumo, lista, clear)


def modelo_eco(modelo, consumo, lista, clear):
    clear()
    i = consumo.index(max(consumo))
    print("O modelo mais econômico é o(a)", modelo[i], "com um consumo de",
          consumo[i], "Kilômetros por litro.")
    menu(modelo, consumo, lista, clear)


def consumo_medio(modelo, consumo, lista, clear):
    clear()
    lista = 0
    media = 0.0
    while lista < 5:

        media = consumo[lista] * 4.99       # erro
        total = media * 1000
        print("O consumo do carro", modelo[lista], "é de", media, "consumindo", 
              total, "reais para percorrer 1000Km")

        lista = lista + 1
    menu(modelo, consumo, lista, clear)


def menu(modelo, consumo, lista, clear):
    print("-------------MENU------------")
    print("1- INSERIR CARRO")
    print("2- REMOVER CARRO")
    print("3- MODELO MAIS ECONÔMICO")
    print("4- CONSUMO MÉDIO")
    print("0- SAIR")
    print("-----------------------------")
    op = int(input("Opção desejada: "))
    print("-----------------------------")

    if op == 1:
        if (lista == 5):
            print("Lista cheia! Remova um para inserir!")
            menu(modelo, consumo, lista, clear)
        else:
            inserir_carro(modelo, consumo, lista, clear)
    elif op == 2:
        remover_carro(modelo, consumo, lista, clear)
    elif op == 3:
        modelo_eco(modelo, consumo, lista, clear)
    elif op == 4:
        consumo_medio(modelo, consumo, lista, clear)
    elif op == 0:
        SystemExit
    elif op != 1 or 2:
        print("Opção inválida! Retornando...")
        print("--------------------------")


menu(modelo, consumo, lista, clear)
