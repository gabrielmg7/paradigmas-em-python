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

5. Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.

- Resposta
    
    ```python
    x = int(input("Insira um número inteiro: "))
    
    if x > 0:
        print(x, "Valor positivo.")
    elif x < 0:
        print(x, "Valor negativo.")
    elif x == 0:
        print(x, "Valor neutro.")
    ```