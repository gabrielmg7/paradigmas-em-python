## PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON
---
#### ESTACIO DE SÁ | FACULDADE INTEGRADA DO CEARÁ | 2022.2
---
##### PROFESSOR: Estevão Pereira
##### ALUNO: Gabriel Moura
##### Data de Entrega: 02/11/2022
##### Avaliando o Aprendizado Ciclo 3
##### [Notion] (https://gabrielmdev.notion.site/AVALIANDO-O-APRENDIZADO-Ciclo-3-90aff1fda8ea43af9e3e1196d5380681)
---
4ª Questão | Ref.: 201908830056 

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

Respondido em 02/11/2022 17:54:47

---
