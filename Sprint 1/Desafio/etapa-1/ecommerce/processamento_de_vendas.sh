#!/bin/bash
cd ~/ecommerce/
# variável de coleta da data do sistema
current_date=$(date +"%Y%m%d")

# cria subdiretórios da pasta ecommerce
mkdir vendas-${current_date}/
cp dados_de_vendas.csv vendas-${current_date}
mkdir vendas-${current_date}/backup

# copia e renomeia o csv dos dados de vendas
cp vendas-${current_date}/dados_de_vendas.csv vendas-${current_date}/backup/dados-${current_date}.csv

#renomeia novamente o arquivo dentro do diretorio backup
mv vendas-${current_date}/backup/dados-${current_date}.csv vendas-${current_date}/backup/backup-dados-${current_date}.csv 

# criação do arquivo relatorio.txt dentro do diretorio backup

{
  echo "Data do sistema operacional: $(date '+%Y/%m/%d %H:%M')"
  echo "Data do primeiro registro de venda: $(head -n 2 vendas-${current_date}/backup/backup-dados-${current_date}.csv | tail -n 1 | cut -d',' -f5)"
  echo "Data do último registro de venda: $(tail -n 1 vendas-${current_date}/backup/backup-dados-${current_date}.csv | cut -d',' -f5)"
  echo "Quantidade total de itens diferentes vendidos: $(cut -d',' -f2 vendas-${current_date}/backup/backup-dados-${current_date}.csv | sort | uniq | wc -l)"
  echo "Primeiras 10 linhas do arquivo backup:"
  head -n 11 vendas-${current_date}/backup/backup-dados-${current_date}.csv
} > vendas-${current_date}/backup/relatorio.txt

# zipar o arquivo backup
zip vendas-${current_date}/backup/backup-dados-${current_date}.zip vendas-${current_date}/backup/backup-dados-${current_date}.csv 

# remover arquivos de dados não zipados
rm vendas-${current_date}/backup/backup-dados-${current_date}.csv
rm vendas-${current_date}/dados_de_vendas.csv


