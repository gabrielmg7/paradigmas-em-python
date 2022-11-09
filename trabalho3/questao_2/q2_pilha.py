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
