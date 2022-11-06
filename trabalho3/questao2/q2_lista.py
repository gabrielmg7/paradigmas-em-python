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