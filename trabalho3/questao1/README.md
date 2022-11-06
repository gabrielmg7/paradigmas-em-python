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
1. Sobre os critérios de avaliação de linguagens de programação, enumere e explique cada critério.

- Resposta:
    1. **Legibilidade:**
        - 90% do tempo o programador está lendo e modificando códigos que já existem;
        - Custos trabalhistas acarretam em curstos com hardware;
        - **Simplicidade:** não deve ter uma sintaxe complexa, muitas formas de resolver um único problema, sobrecarga de métodos, operadores, etc.
        - **Ortogonalidade:** um conjunto relativamente pequeno de construções primitivas pode ser combinado.
        - **Declarações de controle:** deve haver instruções de controle adequadas.
            - O uso do loop `for`, enquanto for um loop, faça enquanto o loop é aplicável;
            - O uso de declarações `go to` causa baixa legibilidade.
        - **Design de sintaxe:** o design da sintaxe afeta a legibilidade do código, como por exemplo
            - Identificadores abreviados é uma barreira à legibilidade;
            - Palavras especiais que são exclusivas da linguagem e podem ser usadas como nomes de variáveis.
                - Ex.: `class`, `int`, `while`…
        - Se alguém não entende o código existente, ele será descartado ou substituido.
    2. **Escritabilidade**:
        - A curva de aprendizado na programação é grande, então uma linguagem em que escreve-se menos é mais produtivo!
        - Facilidade na escrita aumenta a produtividade do programador;
        - Uma solução escrita em algumas linguagens pode ser escrita em menos linhas do que em outras.
        - A maioria das características do idioma que afetam a legibilidade também afetam a Escritabilidade.
        - **Simplicidade:** não deve ter uma sintaxe complexa, muitas formas de resolver um único problema, sobrecarga de métodos, operadores, etc.
        - **Ortogonalidade:** um conjunto relativamente pequeno de construções primitivas pode ser combinado.
        - **Suporte à Abstração**: A linguagem deve suportar a abstração de processos e dados.
        - **Expressividade**: um programa pode ser escrito com menos linhas de código.
            - Declarações `for` fazem a contagem de loops serem mais fáceis que com `while`
            - `i++` é mais expressivo que `i = i + 1`
    3. **Confiabilidade**:
        - V**erificação de Tipagem**: Ele está testando para erro de tipagem, seja em tempo de compilação ou execução.
            - R**efere-se ao teste de compatibilidade de tipo entre duas coisas.**
            - Ex.: É mais desejável a porcentagem `float` do que a porcentagem `int`
        - **Tratamento de Excessões**: é a capacidade de um programa detectar antecipadamente erros durante o tempo de execução, juntamente com resultados desconhecidos e condições incomuns, usar medidas corretivas e continuar e concluir a execução.
        - **Aliasing:** ocorre quando um local de memória (variável) possui mais de um nome ou método de referência apontando para ela.
    4. **Custo**:
        
        O custo para o desenvolvimento do software deve ser o mínimo possível, alcançando o máximo de produtividade. O custo total de uma linguagem de programação é uma combinação de muitos de seus recursos e características. De todos aqueles que contribuem para os custos da linguagem, o desenvolvimento e a manutenção do programa são as considerações mais importantes e, uma vez que são funções de legibilidade e escrita, são por sua vez os mais importantes dos critérios de avaliação. 
        
        Exemplos:
        
        - Tempo para codificar o software;
        - Custo de compilação do software;
        - Custo do hardware necessário;
        - Custo de manutenção do software;
    5. **Generalidade**: A linguagem não deve se limitar apenas a aplicação específica.
    6. **Extensibilidade**: Deve ser flexível, deve ser capaz de adicionar novas builds.
    7. **Padronização**: A linguagem deve ser independente de plataforma.
    8. **Suporte à Internacionalização**: Vários formatos como hora, data, moeda e etc. devem ser suportados.