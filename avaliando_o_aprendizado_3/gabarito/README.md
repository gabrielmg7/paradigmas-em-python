## PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON
---
#### ESTACIO DE SÁ | FACULDADE INTEGRADA DO CEARÁ | 2022.2
---
##### PROFESSOR: Estevão Pereira
##### ALUNO: Gabriel Moura
##### Data de Entrega: 02/11/2022
##### Avaliando o Aprendizado Ciclo 3
##### Link do Projeto no [Notion](https://gabrielmdev.notion.site/AVALIANDO-O-APRENDIZADO-Ciclo-3-90aff1fda8ea43af9e3e1196d5380681)


📜 O **Avaliando o Aprendizado** são exercícios na forma de simulados para todos os alunos dos cursos presenciais que possuem Prova Nacional Integrada (PNI) e Banco de Questões. Ele lhe dá a chance de estudar por meio de quatro simulados realizados ao longo do semestre, além de permitir que você **obtenha até 1,0 ponto extra para utilizar na AV1 e AV2.** Cada ciclo vale até 0,5 pontos de acordo com os acertos. A pontuação final é dividida da seguinte forma:
**Ciclo 1 + Ciclo 2** = Até 1,0 ponto extra na **AV1
Ciclo 3 + Ciclo 4** = Até 1,0 ponto extra na **AV2**



### 1ª Questão | BdQ Ref.: 201908829808 | (CESGRANRIO / UNIRIO, 2019)

O código a seguir exibe parte de um programa Python que tem por objetivo retirar um elemento de uma pilha (variável stack) de strings e exibir no console o valor do elemento retirado.

```python
def empty(s):

    if len(s) == 0:
        return True
    else:
        return False

def pop(s):
		#falta a implementação
		#desta função
		

stack = ['calça', 'meias', 'paletó', 'gravata', 'camisa']

if not empty(stack):
    print(pop(stack))
else:

    print('Pilha vazia')
```

A pilha foi concebida de modo que o seu topo é o primeiro elemento de uma lista (variável stack). Qual versão da função pop(s) fará com que o programa acima alcance o seu objetivo?

- def pop(s): temp=s[0] s.remove(s[0]) return temp
- def pop(s): return s.pop(-1)
- def pop(s):  return s.pop()
- def pop(s): temp=s[-1] s=s[-1:1:-1] return temp
- def pop(s): temp=s[0] s=s[1:] return temp

---


### 2ª Questão | BdQ Ref.: 201907642217

A modularização de programas, também conhecida como a técnica **dividir para conquistar** é muito utilizada no paradigma de programação estruturada. Nesse sentido, os subprogramas possuem código independente e devem ser definidos separadamente no programa. Além disso, precisamos verificar os escopos das variáveis utilizadas as quais podem ser globais ou locais. Levando em consideração seu conhecimento sobre subprogramas na linguagem Python e o escopo das variáveis utilizadas. 

Analise as assertivas em relação ao código abaixo:

```python
def troca(a, b):
    aux = a
    a = b
    b = aux

a = 10
b = 20

troca(a, b)
print(a)
print(b)
```

I - As variáveis a e b são globais, dessa forma, ao executar o subprograma ¿troca¿, elas não teriam seus valores afetados.

II - O programa não iria funcionar pois, obrigatoriamente, os subprogramas devem ser definidos ao final do programa principal quando se utiliza a linguagem Python.

III - As variáveis a e b utilizadas no subprograma são locais, assim, ao executar o subprograma ¿troca¿, elas não afetariam os valores das variáveis a e b definidas globalmente.

Qual(s) afirmativa(s) é (são) verdadeira(s)?

- Apenas I e II.
- I, II e III.
- Apenas II e III.
- Nenhuma das alternativas.
- Apenas I e III.

---


### 3ª Questão | BdQ Ref.: 201908829807 | (AOCP / MJSP, 2020)

Assinale a alternativa que apresenta o código Python que implementa corretamente uma função para o cálculo da área de um retângulo, bem como o código que imprime o seu resultado.

a)

```python
def area_retangulo(comp, larg):
	return comp * larg
	print(' A área é {}' .format
	(area_retangulo (2,4)))
```

b)

```python
def area_retangulo(comp, larg){
	return comp * larg}
	print(' A área é ' +
	area_retangulo (2,4))
```

c)

```python
func area_retangulo(comp, larg): return comp * larg print(' A área é ' ||
area_retangulo (2,4))
```

d)

```python
def area_retangulo(comp, larg)(
return comp * larg);
print(' A área é {}' .format (area_retangulo (2,4)))
```

e)

```python
func area_retangulo(comp, larg): return comp * larg; println(' A área é ' +
	area_retangulo (2,4))
```

---


### 4ª Questão | Ref.: 201908830056

Analise o seguinte trecho de código:

```python
n1 = int(input('Primeiro numero: '))
n2  = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))
print(n1,'-',n2,'-',n3)
if(n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux
if(n2 > n1):
    aux = n2
    n2 = n1
    n1 = aux
if(n3 > n2):
    aux = n3
    n3 = n2
    n2 = aux    
print(n1,'-',n2,'-',n2)
```

- O programa apresentará erro caso o usuário entre com números iguais
- O programa apresentará um erro no comando input
- O programa irá ordenar os números em ordem crescente
- O programa apresentará um erro pois está utilizando a variável aux de forma global
- O programa irá ordenar os números em ordem decrescente

---


### 5ª Questão | Ref.: 201907579269

Expressões condicionais são muito utilizadas em linguagens de programação quando um programa necessita tomar decisões sobre qual comando será executado. Python, assim como quase todas as linguagens de programação, propicia que o programador utilize as estruturas condicionais de forma que um programa possa realizar essa decisão. Nesse contexto, suponha que um programador desenvolveu um programa em Python que verifique se um aluno tirou nota abaixo de 7.0 e maior que 4.0 e nesse caso, ele então poderá realizar uma segunda  prova para tentar obter a sua aprovação:

```python
a = input("Digite sua nota: ")
nota = float(a)

if nota >= 7.0:
    print("Você está aprovado por média.")
    if nota > 9.0:  # IF ANINHADO
        print("Parabéns!")  # se nota > 9
    print("Boas Férias!")  #  se nota >=7
else:
    if nota >= 4:  # IF ANINHADO
        print("Você pode fazer G2.")
        print("Venha na próxima semana.")
    else:
        print("Você está reprovado!")
        print("Você não pode fazer G2.")
print("Acabou.")
```

Caso o usuário entre com a nota 6.5, quais as saídas que o programa acima irá exibir?

- Você está reprovado. Acabou.
- Parabéns! Boas Férias. Acabou.
- Você pode fazer G2. Boas Férias! Acabou.
- Você pode fazer G2.  Venha na próxima semana. Acabou.
- O programa não irá funcionar pois o comando input recebe apenas valores literais.