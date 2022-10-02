#coding: utf-8

x = float(input("| Insira o valor de X: "))
y = float(input("| Insira o valor de Y: "))
if (x == "") or (y ==""): 
    print("Insira um valor para X e Y.")
else:
    print("| Resultado:", "%.1f" % (x+y))