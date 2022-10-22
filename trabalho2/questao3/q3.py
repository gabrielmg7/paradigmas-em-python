nome_out = []
idade_out = []
len = 0

def inserir(nome_out, idade_out, lista):
    while lista < 5:
        nome_in = input("Insira o nome: ")
        idade_in = input("Insira a idade: ")
        nome_out.append(nome_in)
        idade_out.append(idade_in)
        lista = lista + 1
print()

def remover(lista):
    op = int(input("Qual a posição que você deseja remover?"))
    lista.pop(op)
    
insere(nome_out, idade_out)
remove()