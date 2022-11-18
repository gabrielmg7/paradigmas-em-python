## PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON
---
#### ESTACIO DE SÁ | FACULDADE INTEGRADA DO CEARÁ | 2022.2
---
##### PROFESSOR: Estevão Pereira
##### ALUNO: Gabriel Moura
##### Data de Entrega: 02/11/2022
##### Avaliando o Aprendizado Ciclo 3
##### Link do Projeto no [Notion](https://gabrielmdev.notion.site/AVALIANDO-O-APRENDIZADO-Ciclo-3-90aff1fda8ea43af9e3e1196d5380681)
---
2ª Questão | BdQ Ref.: 201907642217

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

Respondido em 02/11/2022 17:43:17

---
