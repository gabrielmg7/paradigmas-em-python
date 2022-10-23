modelo = []
consumo = []
lista = 0


def inserir_carro(modelo, consumo, lista):
    while lista < 5:
        modelo.append(input("Insira o Modelo do carro: "))
        consumo.append(input("Insira quantos Km/litro: "))
        lista = lista + 1
        print("--------------------------")
        print("Modelo: ", modelo)
        print("Consumo: ", consumo)
        print("--------------------------")
    modelo_eco(modelo, consumo)
    


def remover_carro(modelo, consumo, lista):
    op = int(input("Qual carro deseja remover? (0-4:) "))
    if op != (0 - 4):
        print("Opção inválida! Retornando...")
        menu(modelo, consumo, lista)
    else:
        modelo.pop(op)
        consumo.pop(op)
    print("--------------------------")
    print("Modelo: ", modelo)
    print("Consumo: ", consumo)
    print("--------------------------")


def modelo_eco(modelo, consumo):
    i = modelo.index(min(consumo))
    print("O modelo mais econômico é o(a)", modelo[i], "com um consumo de", consumo[i])


def menu(modelo, consumo, lista):
    print("----------MENU----------")
    print("1- INSERIR CARRO")
    print("2- REMOVER CARRO")
    print("3- SAIR")
    print("------------------------")
    op = int(input("Opção desejada: "))
    if op == 1:
        if (lista == 5):
            print("Lista cheia! Remova um para inserir!")
            menu(modelo, consumo, lista)
        else:
            inserir_carro(modelo, consumo, lista)
    elif op == 2:
        remover_carro(modelo, consumo, lista)
    elif op == 0:
        SystemExit
    elif op != 1 or 2:
        print("Opção inválida! Retornando...")
        print("--------------------------")
        


menu(modelo, consumo, lista)
