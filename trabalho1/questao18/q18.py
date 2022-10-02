#coding: utf-8

n1 = float(input("Insira a nota da AP1: "))
n2 = float(input("Insira a nota da AP2: "))
n3 = float(input("Insira a nota da AP3: "))
n4 = float(input("Insira a nota da AP4: "))
print("\n")

def imprimir(n1, n2, n3, n4):
    media = (n1+n2+n3+n4)//4

    print("Nota da AP1:", n1, "\n---------------")
    print("Nota da AP2:", n2, "\n---------------")
    print("Nota da AP3:", n3, "\n---------------")
    print("Nota da AP4:", n4, "\n---------------")
    print("Média de notas do Aluno: ", media)

if (n1 == "") or (n2 == "") or (n3 == "") or (n4 == ""):
    print("ERRO! Você deve inserir todas as notas para calcular a média anual.")
else:
    imprimir(n1, n2, n3, n4)