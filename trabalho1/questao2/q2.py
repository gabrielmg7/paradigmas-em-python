# converter dólares em reais, mas se o cliente desejar trocar mais de 100 dólares, dar 10% de desconto no valor do dólar.

cot = float(input("Cotação atual do dólar: "))
valor = float(input("Valor a ser convertido: "))
res = valor*cot
print ("Convertendo...\n")
print ("Saldo: R$" + res)
