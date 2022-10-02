#coding: utf-8

import sys

nome = ""
idade = 0
salario = 0.0
sexo = ""
estadoCivil = ""

def inputNome(nome):
    if(len(nome) < 3):
        print("BEEEEP! Deve ter mais de 3 caracteres. \n")
        inputNome(nome)
    else:
        print("Beep-Bop... VALIDADO!! \n")
#---------------------------------------------------------------------------------------------------
def inputIdade(idade):
    if(idade > 150) and (idade < 0):
        print("BEEEEP! É um humano mesmo? Deve ter menos de 150 anos!\n")
        inputIdade(idade)
    else:
        print("Beep-Bop... VALIDADO!! \n")
#---------------------------------------------------------------------------------------------------
def inputSalario(salario):
    if (salario <= 0):
        print("BEEEEP! Escravidão? Deve ser maior que 0!")
        inputSalario(salario)
    else:
        print("Beep-Bop... VALIDADO!!")
#---------------------------------------------------------------------------------------------------
def inputSexo(sexo):
    sexo = str(input("Insira o sexo(m/f): "))
    if(sexo == 'm'):
        print("M -> Masculino")
    elif(sexo == 'f'):
        print("F -> Feminino")
    elif(sexo == ""):
        ("BEEEEP! Insira o sexo!")
        return inputSexo(sexo)
    elif(sexo != 'm') or (sexo != 'f'):
        print("BEEEEP! Apenas Feminino ou Masculino!")
        sexo = ""
        return inputSexo(sexo)
    else:
        print("Beep-Bop... VALIDADO!! \n")
#---------------------------------------------------------------------------------------------------
def inputEstadoCivil(estadoCivil):
    if(estadoCivil != 's') or (estadoCivil != 'c') or (estadoCivil != 'v') or (estadoCivil != 'd'):
        print("BEEEEP! Solteiro(a), Casado(a), Viúvo(a) ou Divorciado(a)?")
    else:
        print("Beep-Bop... VALIDADO!!")
#---------------------------------------------------------------------------------------------------

#CHAMADA DAS FUNÇÕES

nome = str(input("Insira o nome: "))
inputNome(nome)
idade = int(input("Insira a idade: "))
inputIdade(idade)
salario = float(input("Insira o salário: "))
inputSalario(salario)
inputSexo(sexo)
estadoCivil = str(input("Estado Civil(s/c/v/d): "))

sys.exit("Dados Validados! Saindo...")