#coding: utf-8

numero = 0;
soma = 0;

for numero in range(0, 100, 1):
    if numero % 2 == 0:            
        print("| Valor:", numero)
        res = soma + numero
        print("| Soma:", soma, "+", numero, "=", res, "\n|------------------------")
        soma = res
    