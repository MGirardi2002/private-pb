
# O Desafio Final: Dashboard no AWS QuickSight

Agora, será evidenciado e explicado toda a trajetória de desenvolvimento do dashboard final do desafio do programa de bolsas.

# Etapas

## Correção de algumas coisas antes de começar...

Antes de iniciar a produção do dashboard, gostaria de esclarecer que realizei algumas alterações nos dados em relação ao que foi feito nas sprints 8 e 9. De forma resumida, reestruturei os conjuntos de dados para melhor organização, separando-os em tabelas que representam as dimensões e a tabela fato. Além disso, adicionei uma coluna que anteriormente estava faltando para aprimorar a análise. Abaixo, estão os prints dos jobs utilizados e do novo modelo dimensional.

![Etapa I](../evidencias/01job.png)
![Etapa I](../evidencias/02job.png)
![Etapa I](../evidencias/03job.png)
![Etapa I](../evidencias/04modelo.png)

## Relação de Joins

Aqui está a representação das ligações dos conjuntos de dados, basicamente, a tabela fato_filme da Left Join em todas as outras dimensões usando o id como chave primária;
![Etapa I](../evidencias/05qs.png)

## Introdução do Dashboard

A primeira página do dashboard serve como uma introdução para a análise, que se baseia em uma amostra de 4698 filmes de Ficção Científica, e é destinada a investigar a popularização do tema de filmes sobre alienígenas, levando como ponto de pesquisa o lançamento do primeiro filme da franquia "Alien", de 1979.

De início já se faz uma comparação com a média de popularidade dos filmes na amostra (10,28) e especificamente daqueles que mencionam "Alien" em suas sinopses (15,3), e foi utilizado um filtro nos dados de 'overview' para a palavra-chave. Também é evidenciado a média de orçamento geral de todos os filmes da amostra, bem como a média para cada ano (do filme mais velho para o filme mais novo), em dólares americanos.

![Etapa I](../evidencias/06qs.png)
