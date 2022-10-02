#coding: utf-8

vetor = []
consoantes = []
total = 0

while(len(vetor) < 10):
    letra = str(input("Insira uma letra: "))
    if letra in 'bBcCdDfFgGjJkKlLmMnNpPqQrRsStTvVwWxXzZ ':
        consoantes.append(letra)
        total = total + 1
    vetor.append(letra)
print("\n São", total, "consoantes.", consoantes)