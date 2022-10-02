#coding: utf-8

x = float(input("| Insira o valor de X: "))
y = float(input("| Insira o valor de Y: "))
if (x == "") or (y == ""): 
    print("Insira um valor para X e Y.")

if (x > y):
    print("| O maior deles é X = ", x)
elif(x < y):
    print("| O maior deles é Y = ", y)
elif(x == y):
    print("| X = Y")