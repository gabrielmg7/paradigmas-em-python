#coding: utf-8

num = int(input("Insira o valor a ser calculado: "))

res = 1 
count = 1
for n in range(1, num + 1):
    res *= n

print("Resultado:", res)