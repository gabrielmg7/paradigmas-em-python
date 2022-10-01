num = float(input("Insira o valor a ser calculado: "))
print("|----------------")
print("| Resultado: ")
print("|----------------")
for i in range(1,11):

    r = i*num    

    print("| {} x {} = {}".format(num,i,r))    
    i = i+1
print("|---------------")