#calular a área  e o perímetro de um retângulo

b = input("Digite a base do Retângulo: ")
b1 = int(b)
h = input("Digite a altura do Retângulo: ")
h1 = int(h)

p = (2*b1) + (2*h1)
a = b1*h1

if(a=="") or (b==""):
    print("Você deve inserir um valor para A e B.")
else:
    print("Área:", a)
    print("Perímetro:", p)
