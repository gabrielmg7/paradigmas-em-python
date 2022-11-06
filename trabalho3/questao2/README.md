## PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON
---
### ESTACIO DE SÁ | FACULDADE INTEGRADA DO CEARÁ | 2022.2
##### 👨🏻‍💻 **Aluno**: Gabriel M. Guimarães
##### 📋 **Matrícula**: 201902661559
##### 👨🏾‍🏫 **Professor**: Estevão Pereira
##### 📆 **Data**: 04/11/2022
##### 🎯 Valendo 2.5 Pontos na AV2
##### 🔗 Link do Projeto no [Notion](https://gabrielmdev.notion.site/Trabalhos-5baf7d4988a846159411739b739fcc30)
---
#### Questão 2: Diferencie Listas, tuplas e dicionários em python. Dê exemplos.


📄 **Lista**: é uma estrutura de dados indexados e armazenados em sequência, onde cada elemento possui uma posição que é identificada por um índice.

```python
exemplo = ["x1", "x2", "x3"]

# Também é possível criar uma lista dentro de outra (nested list).
exemplo2 = ["x1", [ "x2", "x3", "x4"]]

# Acessando valores:
a1 = exemplo[0] # a1 = índice 0

# Listas são mutáveis.
exemplo[1] = "y2" # atribui outro valor para a variável de índice 1

# Inserindo elementos:
exemplo.append("x4") # com a função .append() insere-se no final da lista
exemplo.insert(4, "x5") # com a função .insert() insere-se na posição informada

# Removendo elementos:
exemplo.remove("x5") # com a função .remove() deve-se invormar o valor
exemplo.pop(3)       # com a função .pop() deve-se informar o índice
```

---
🔋 **Pilha**:

```python
class Stack:

    def __init__(self):
        self.lista = []  

    # inserindo elemento
    def push(self, el):
        self.lista.apend(el)
    
    # remove e retorna o último elemento
    def pop(self):
        return self.lista.pop()

    # verificar se a pilha está vazia
    def isEmpty(self):
        return (self.lista == [])
```

---


📖 **Dicionários**: são estruturas que compreendem um conjunto de pares: chave e valor. Cada chave individual possui um valor associado. Esse tipo de associação se dá o nome de coleção associativa desordenada.

```python
# x1 é a chave do valor a1 
# x2 é a chave do valor b1
exemplo = {"x1": "a1", "x1": "a2", "x2": "b1", "x2": "b2", "x3": "c1", "x3": "c2"}

# Acessando elementos (usa-se a chave associativa):
valores_b = exemplo["x2"] # Atribui-se à uma variável

# Também é possível acessar um elemento do dicionário por meio do método get. 
# informa-se a chave do elemento e uma mensagem de retorno caso não haja nada.
valores_c = exemplo.get("c1", "Não encontrado.")

# Adicionando u{m elemento ao dicionário
exemplo.update({"x3":"c4"}) # função .update() passa-se como parâmetro a chave com o valor a ser associado.
exemplo["x1"] = "a3" # associando um valor diretamente à chave 

#Removendo um elemento do dicionário 
exemplo.pop("x2")  # pela função .pop() 
del exemplo["x1"] # pela função .del()

```

