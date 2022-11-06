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

9. **Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:**
    
    **a. Mostre a quantidade de valores que foram lidos;**
    
    **b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;**
    
    **c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;**
    
    **d. Calcule e mostre a soma dos valores;**
    
    **e. Calcule e mostre a média dos valores;**
    
    **f. Calcule e mostre a quantidade de valores acima da média calculada;**
    
    **g. Calcule e mostre a quantidade de valores abaixo de sete;**
    
    **h. Encerre o programa com uma mensagem.**
    
    - Resposta
        
        ```python
        notas = []
        acima_media = []
        abaixo_sete = []
        contador = 0
        soma = 0
        nota = int(input("Digite a nota: "))
        
        while nota != -1:
            if nota >= 0 and nota <= 100:
                notas.append(nota)
                soma = soma + nota
                contador += 1
                media = soma / contador
                if nota > media:
                    acima_media.append(nota)
                if nota < 7:
                    abaixo_sete.append(nota)
        
            nota = int(input("Digite a nota: "))
        
        print("#######################")
        print("Quantidade de elementos:", contador)
        print("Notas:", notas)
        print("Notas:", notas.reverse())
        print("Média:", media)
        print("Acima da Média:", acima_media)
        print("Maiores que 7:",  abaixo_sete)
        print("#######################")
        print("Fim do programa.")
        ```