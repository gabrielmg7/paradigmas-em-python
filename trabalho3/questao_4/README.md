## PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON
---
### ESTACIO DE SÁ | FACULDADE INTEGRADA DO CEARÁ | 2022.2
##### 👨🏻‍💻 **Aluno**: Gabriel M. Guimarães
##### 📋 **Matrícula**: 201902661559
##### 👨🏾‍🏫 **Professor**: Estevão Pereira
##### 📆 **Data**: 04/11/2022
##### 📋 Atividade Complementar 3
##### 🎯 Valendo 2.5 Pontos na AV2
##### 🔗 Link do Projeto no [Notion](https://gabrielmdev.notion.site/Trabalhos-5baf7d4988a846159411739b739fcc30)
---

4. Faça um programa possui uma função que receba um número digitado pelo usuário e calcule a soma de todos os números de 1 até ao número digitado.
    
    Por exemplo, se o usuário digitou o número 4, a saída deve ser 10 (1+2+3+4=10).
    
    - Resposta
        
        ```python
        resultado = 0
        
        numero = int(input("Insira um número: "))
        
        for i in range(1, numero + 1, 1):
            resultado += i
        print("Resultado = ", resultado)
        ```