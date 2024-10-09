
# Resumo

Nesta sprint, o foco foi higienizar a camada Raw do bucket S3, utilizando jobs do AWS Glue para transformar dados brutos em um formato padronizado e limpo, armazenando-os na camada Trusted no formato Parquet. Utilizamos PySpark para leitura e manipulação dos dados, com comandos como trim() para limpar espaços em branco, filter() para filtrar gêneros específicos, como "Sci-Fi", entre outros comandos..


# Exercícios

## Geração e massa de dados

Primeiro, foi requisitado dois warmups simples de randomização, listas e geração de arquivo csv.
![WarmUp1.](exercicios/warmup1.png)

![WarmUp2.](exercicios/warmup2.png)

![WarmUp2Evidence.](exercicios/animaiscsv.png)

Após isso, o exercício de verdade começa. Nele, era necessário gerar um arquiv com 10 milhões de nomes aleatórios, usando a lib names, que foi baixada em uma venv. Primeiramente, requisitava 3000 nomes únicos para armazenar em uma lista, com a função get_full_name(); Então, escolhendo aleatoriamente combinações dos nomes da lista aux, ele armazena em dados e 10 milhões de combinações, e então escreve no arquivo nomes_aleatorios.txt.

![WarmUp2Evidence.](exercicios/ex01.png)

![WarmUp2Evidence.](exercicios/nomesaleatorios.png)
