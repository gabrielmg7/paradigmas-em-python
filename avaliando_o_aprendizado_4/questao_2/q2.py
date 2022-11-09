# Suponha que nessa linguagem seja definida uma função F(A,B) 
# onde A e B são os parâmetros formais, sendo que A é passado por valor,
#  e B é passado por referência. Durante a execução de F,#  somamos 2 ao
# valor de A e subtraímos 2 do valor de B. Caso F(X,Y) seja uma chamada 
# da função, ao longo do programa, onde os parâmetros reais X e Y 
# são variáveis cujos valores antes da chamada são, respectivamente,
#  10 e 20, esperamos que, ao terminar a função, os novos valores de X e Y sejam, respectivamente:

def f(a, b):
    