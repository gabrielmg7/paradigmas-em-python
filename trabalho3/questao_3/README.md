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

3. **Apresente o desenvolvimento das seguintes funções na linguagem de programação python:**
    
    **a. Cálculo do cubo de um número real x.**
    
    - Resposta:
        
        ```python
        x = float(input("Insira um valor: "))
        res = x**3
        print("Raiz Cúbica:", res)
        ```
        
    
    **b. Retorna o terceiro elemento de uma lista.**
    
    - Resposta:
        
        ```python
        lista = ["dolar", "real", "euro", "libra", "peso"]
        print("Terceiro elemento:", lista[2])
        ```
        
    
    **c. Cálculo do fatorial de um número.**
    
    - Resposta:
        
        ```python
        def fatorial(x):
            if x < 0:
                print("Fatorial de um negativo não existe!")
        
            elif x == 0:
                return 1
        
            else:
                res = 1
                while (x > 1):
                    res *= x
                    x -= 1
                return res
        
        x = int(input("Insira um número: "))
        print("Fatorial de", x, "é", fatorial(x))
        ```
        
    
    **d. Soma de todos os elementos de uma lista.**
    
    - Resposta:
        
        ```python
        lista = [23.5, 65.5, 43.1, 89.7, 37.7]
        print ("Lista:", lista)
        print("Soma dos elementos:", sum(lista))
        ```