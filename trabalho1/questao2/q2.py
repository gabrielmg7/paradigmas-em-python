# converter dólares em reais, mas se o cliente desejar trocar mais de 100 dólares, dar 10% de desconto no valor do dólar.

cot = float(input("Cotação atual do dólar: R$"))
valor = float(input("Valor a ser convertido em Reais: US$"))

def imprimir(cot, valor):
    res = 0
    print("Convertendo...\n")
    res = valor * cot
    print("Saldo: R$", "%.2f" % res)

if (cot==""):
    print("BEEEEP! Insira a cotação atual para calular o valor convertido.")

elif(valor==""):
    print("BEEEEP! Insira o valor a ser calculado.")

if(valor > 100.00):
    desconto = cot * 0.10
    cot = cot - desconto
    imprimir(cot, valor)

else:
    imprimir(cot, valor)