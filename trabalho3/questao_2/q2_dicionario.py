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