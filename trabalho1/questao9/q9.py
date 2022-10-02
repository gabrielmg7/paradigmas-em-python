#coding: utf-8

m = float(input("Insira o valor em Metros: "))
cm = m * 100

if (m == ""):
    print("ERRO! Você deve inserir um valor para calular.")
else:
    print("O valor em Centímetros é: ", "%.2f" % cm, "cm")