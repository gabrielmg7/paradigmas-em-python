
r = float(input("Insira o Raio (cm): "))

if (r == ""):
    print("ERRO! Você deve inserir um valor para calular.")
else:
    a = 3.14 * (r * r)
    print("A área deste círculo é:", "%.2f" % a, "cm")