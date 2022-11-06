notas = []
acima_media = []
abaixo_sete = []
contador = 0
soma = 0
nota = int(input("Digite a nota: "))

while nota != -1:
    if nota >= 0 and nota <= 100:
        notas.append(nota)
        soma = soma + nota
        contador += 1
        media = soma / contador
        if nota > media:
            acima_media.append(nota)
        if nota < 7:
            abaixo_sete.append(nota)

    nota = int(input("Digite a nota: "))

print("#######################")
print("Quantidade de elementos:", contador)
print("Notas:", notas)
print("Notas:", notas.reverse())
print("Média:", media)
print("Acima da Média:", acima_media)
print("Maiores que 7:",  abaixo_sete)
print("#######################")
print("Fim do programa.")
