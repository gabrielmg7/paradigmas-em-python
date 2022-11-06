print("Responda com sim ou nao:")

perguntas = [
    "Telefonou para a vítima? ", "Esteve no local do crime? ",
    "Mora perto da vítima? ", "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

pessoa = ["Inocente", "Suspeita", "Cúmplice", "Assassino"]

periculosidade = 0

for i in range(len(perguntas)):
    res = input(perguntas[i])

    if res == "sim":
        periculosidade = periculosidade + 1

if periculosidade == 2:
    print("Você é", pessoa[1])

if periculosidade == (3 or 4):
    print("Você é", pessoa[2])

if periculosidade == 5:
    print("Você é", pessoa[3])

if periculosidade == 0:
    print("Você é", pessoa[0])
