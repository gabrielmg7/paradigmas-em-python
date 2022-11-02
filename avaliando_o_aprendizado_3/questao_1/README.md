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
1ª Questão | BdQ Ref.: 201908829808 | (CESGRANRIO / UNIRIO, 2019) 

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

Respondido em 02/11/2022 17:13:52

---