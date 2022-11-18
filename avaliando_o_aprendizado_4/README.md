## PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON
---
#### ESTACIO DE SÁ | FACULDADE INTEGRADA DO CEARÁ | 2022.2
---
##### PROFESSOR: Estevão Pereira
##### ALUNO: Gabriel Moura
##### Data de Entrega: 
##### Avaliando o Aprendizado Ciclo 4

📜 O **Avaliando o Aprendizado** são exercícios na forma de simulados para todos os alunos dos cursos presenciais que possuem Prova Nacional Integrada (PNI) e Banco de Questões. Ele lhe dá a chance de estudar por meio de quatro simulados realizados ao longo do semestre, além de permitir que você **obtenha até 1,0 ponto extra para utilizar na AV1 e AV2.** Cada ciclo vale até 0,5 pontos de acordo com os acertos. A pontuação final é dividida da seguinte forma:
**Ciclo 1 + Ciclo 2** = Até 1,0 ponto extra na **AV1
Ciclo 3 + Ciclo 4** = Até 1,0 ponto extra na **AV2**


---
### 1ª Questão Ref.: 201908829899 (NC-UFPR / ITAIPU BINACIONAL, 2017)

Sejam os seguintes comandos python executados na sequência apresentada:

```python
x = range(10)

def somar(x,y):
	return x+y

x = [i**2 for i in x if i%2==0]

reduce(somar, x)
```

- 20
- 120
- 45
- 285
- 90

---

### 2ª Questão Ref.: 201908829995 (CESGRANRIO / FINEP, 2014)

Uma linguagem de programação permite que os parâmetros de uma função sejam passados por valor ou por referência. Suponha que nessa linguagem seja definida uma função F(A,B) onde A e B são os parâmetros formais, sendo que A é passado por valor, e B é passado por referência. Durante a execução de F, somamos 2 ao valor de A e subtraímos 2 do valor de B.
Caso F(X,Y) seja uma chamada da função, ao longo do programa, onde os parâmetros reais X e Y são variáveis cujos valores antes da chamada são, respectivamente, 10 e 20, esperamos que, ao terminar a função, os novos valores de X e Y sejam, respectivamente,

- 10 e 20
- 12 e 18
- 12 e 20
- 10 e 18
- 10 e 22

---

### 3ª Questão Ref.: 201908773441

Analise as assertivas a seguir sobre as linguagens de programação C, C++, Python e Java.

I. A linguagem Python é uma linguagem interpretada e imperativa;

II. Java, assim como C++, é um exemplo de linguagem que segue o paradigma de orientação a objetos;

III. O identificador % é utilizado para identificar um comentário que utiliza somente uma linha em um programa escrito na linguagem C;

IV. A linguagem de programação JAVA não fornece suporte à criação de tipos definidos pelo usuário.

A opção referente às assertivas CORRETAS.

Estão corretas somente as assertivas III e IV.

Estão corretas somente as assertivas I e II.

Está correta somente a assertiva I.

Estão corretas somente as assertivas I e III.

Estão corretas somente as assertivas II e IV.

---

### 4ª Questão Ref.: 201908144267

Considere o trecho de código apresentado a seguir.

```python
valores = [1,2,3,4,5,6]
funcaox = lambda x: filter(lambda item: item%2==0, x) * 3
print(funcaox(valores))
```

Qual será a saída apresentada pela execução do código?

- [2, 4, 6, 2, 4, 6, 2, 4, 6]
- [1, 3, 6]
- [6, 12, 18]
- [2, 4, 6]
- [2, 2, 2, 4, 4, 4, 6, 6, 6]

---

### 5ª Questão Ref.: 201908774594

No python a estrutura "for loop" pode ser utilizada para percorrer uma lista de elementos. Considerando isso, selecione a alternativa que apresenta a sintaxe correta da utilização do comando 'for loop' no python.

ITEM A. 

```python
names = ["John", "Sophie", "Junior"]

for x in names:
	print(x)
```

ITEM B. 

```python
for x = ["John", "Sophie", "Junior"]:

print(x)
```

ITEM C.

```python
names = {{"John"}, {"Sophie"}, {"Junior"}}

for x in names:

 print(names)
```

ITEM D.

```python
array.names("John", "Sophie", "Junior")

for x print(names[x]):

end for:
```

ITEM E.

```python
array (["John"],["Sophie"],["Junior"])

for each i = 0 to array[i]

 print (array[i])
```

---