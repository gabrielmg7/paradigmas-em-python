## PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON
---
#### ESTACIO DE SÁ | FACULDADE INTEGRADA DO CEARÁ | 2022.2
---
##### PROFESSOR: Estevão Pereira
##### ALUNO: Gabriel Moura
##### Data de Entrega: 
##### Avaliando o Aprendizado Ciclo 1

<aside>
📜 O **Avaliando o Aprendizado** são exercícios na forma de simulados para todos os alunos dos cursos presenciais que possuem Prova Nacional Integrada (PNI) e Banco de Questões. Ele lhe dá a chance de estudar por meio de quatro simulados realizados ao longo do semestre, além de permitir que você **obtenha até 1,0 ponto extra para utilizar na AV1 e AV2.** Cada ciclo vale até 0,5 pontos de acordo com os acertos. A pontuação final é dividida da seguinte forma:
**Ciclo 1 + Ciclo 2** = Até 1,0 ponto extra na **AV1
Ciclo 3 + Ciclo 4** = Até 1,0 ponto extra na **AV2**

</aside>

### 1ª Questão

Existem muitas linguagens de programação disponíveis no mercado com as mais diversas características e aplicações. No entanto, as linguagens de programação, possuem restrições de tipos de estrutura de controle, estrutura de dados e abstrações que podem ser utilizadas. Nesse contexto, análise as afirmações a seguir:

I - Ao aprender várias linguagens de programação, é possível que um problema possa ser resolvido mais facilmente devido a adequação a uma linguagem específica.

II - Não há necessidade de se aprender mais do que uma linguagem de programação haja vista que as estruturas possuem equivalentes em todas elas

III - Aprender diversas linguagens de programação propicia um melhor embasamento para decidir qual deve ser utilizada para resolver um determinado problema.

É (são) verdadeira(s):

- I e III
- I e II
- Todas são verdadeiras
- II e III
- Nenhuma afirmação é verdadeira

---

Respondido em 21/09/2022 19:16:55

---

### 2ª Questão

Analise o texto a seguir:

"Quanto mais você conhece uma linguagem, mais fácil se torna aprender uma segunda, além disso, linguagens de programação são dinâmicas devemos estar preparados para aprender linguagens diferentes".

De acordo com o texto assinale a alternativa que apresenta a razão para estudar linguagens de programação:

- Avanço geral da computação.
- Melhor uso de linguagens conhecidas.
- Aumento da capacidade de expressar ideias.
- Embasamento para escolher linguagens adequadas.
- Aumento da habilidade para aprender novas linguagens.

---

Respondido em 21/09/2022 19:17:11

---

### 3ª Questão

Aprender linguagens de programação se tornou indispensável na nossa sociedade.  Segundo reportagem publicada no Olhar Digital: 

<aside>
📄 “A necessidade de um segundo idioma é praticamente indispensável para que o profissional se mantenha competitivo no atual mercado de trabalho. Seja qual for a área de atuação. E isso não é de hoje. Se você não fala inglês ou espanhol, pode ter certeza: seu currículo vai ficar ali, separado em um segundo bloco. A novidade é que está chegando a hora de se preparar para aprender mais uma linguagem: programação, é o idioma da inovação. E promete se tornar habilidade básica do profissional do futuro. Ou até já do presente.”

*Disponível em: [https://olhardigital.com.br/2020/05/23/videos/programacao-passa-a-ser-diferencial-em-multiplas-areas-do-mercado-de-trabalho-2/](https://olhardigital.com.br/2020/05/23/videos/programacao-passa-a-ser-diferencial-em-multiplas-areas-do-mercado-de-trabalho-2/). Acessado em: 19/01/2021.*

</aside>

Nesse sentindo, qual(s) das vantagens abaixo podem ser relacionadas a habilidades que podem ser adquiridas ao aprender várias linguagens de programação?

I - Aumento da capacidade de expressar ideias

II - Melhor entendimento da importância da implementação

III - Ser especialista em Inteligência Artificial

- I e II
- I e III
- Todas
- II e III
- Apenas I

---

Respondido em 21/09/2022 19:20:00

---

### 4ª Questão

Em um sistema computacional baseado na arquitetura de Von Neumann há sempre um bloco de memória que é utilizado para armazenar valores que serão posteriormente trabalhados pela unidade de processamento ou então serão exibidos em um dispositivo de saída. Diretamente ligado a esse bloco de memória, temos o conceito de variável que pode ser entendimento como uma abstração desse bloco. Entretanto, existem alguns atributos que são utilizados para caracterizar uma variável. Qual das opções abaixo apresenta atributos relacionados com o conceito de variável?

- nome, forma, valor, tamanho
- nome, arquitetura, tipo, valor
- nome, endereço, tipo, valor
- arquitetura, tipo, endereço, valor
- tamanho, arquitetura, endereço, valor

---

Respondido em 21/09/2022 19:20:34

---

### 5ª Questão

Em um certo exercício, um professor pediu para fazer uma função em Python para receber uma lista e imprimir o maior elemento da lista. Abaixo está o código de seu colega.

```python
def maiorDaLista(lista):
    n = len(lista)
    aux = lista[0]
    ind = 0
    for i in range(lista):
        if aux:
            aux = lista[i]
            ind = i
    return aux

#teste
l = [3, 6, 1, 7, 4]
maior = maiorDaLista(l)
print("maior valor:", maior, ", indice na lista", ind)
```

Seu colega aponta que está ocorrendo um erro durante a execução do código. Esse erro é decorrente do fato de:

A variável maior ser igual a zero

A variável l não ser do tipo lista

o ind no print ter escopo local e não global

A virgula dentro da string ", indice" é um caracter inválido

Ele ter chamado a função com o nome errado

---

Respondido em 21/09/2022 19:22:32

---