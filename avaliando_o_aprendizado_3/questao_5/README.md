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
5a Questão | Ref.: 201907579269

Expressões condicionais são muito utilizadas em linguagens de programação quando um programa necessita tomar decisões sobre qual comando será executado. Python, assim como quase todas as linguagens de programação, propicia que o programador utilize as estruturas condicionais de forma que um programa possa realizar essa decisão. Nesse contexto, suponha que um programador desenvolveu um programa em Python que verifique se um aluno tirou nota abaixo de 7.0 e maior que 4.0 e nesse caso, ele então poderá realizar uma segunda  prova para tentar obter a sua aprovação:

```python
a = input("Digite sua nota: ")
nota = float(a)

if nota >= 7.0:
    print("Você está aprovado por média.")
    if nota > 9.0:  # IF ANINHADO
        print("Parabéns!")  # se nota > 9
    print("Boas Férias!")  #  se nota >=7
else:
    if nota >= 4:  # IF ANINHADO
        print("Você pode fazer G2.")
        print("Venha na próxima semana.")
    else:
        print("Você está reprovado!")
        print("Você não pode fazer G2.")
print("Acabou.")
```

Caso o usuário entre com a nota 6.5, quais as saídas que o programa acima irá exibir?

- Você está reprovado. Acabou.
- Parabéns! Boas Férias. Acabou.
- Você pode fazer G2. Boas Férias! Acabou.
- Você pode fazer G2.  Venha na próxima semana. Acabou.
- O programa não irá funcionar pois o comando input recebe apenas valores literais.
