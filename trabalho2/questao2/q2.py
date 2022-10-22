
def soma(x, y):
  print("Resultado: ",x + y)

def subtracao(x, y):
  print("Resultado: ",x - y)

def multiplicacao(x, y):
  print("Resultado: ",x * y)

def divisao(x, y):
   print("Resultado: ",x / y)    

def main():
    x = float(input("Primeiro número: "))
    y = float(input("Segundo número: "))
    op = int(input("Operação desejada: ")) 
    if op == 1:
        soma(x, y)
    elif op == 2:
        subtracao(x, y)
    elif op == 3:
        multiplicacao(x, y)
    elif op == 4: 
        divisao(x, y)
    elif op != (1 or 2 or 3 or 4):
        print("Opção inválida! Escolha de 1 a 4.")
        print("Retornando para Main...")
        main()
main()
