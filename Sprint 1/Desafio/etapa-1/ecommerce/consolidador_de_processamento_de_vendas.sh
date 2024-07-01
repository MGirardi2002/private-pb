#!/bin/bash

# cria arquivo relatorio_final.txt
touch relatorio_final.txt

# laço de repetição para percorrer os diretorios vendas-*
for dir in vendas-*; do
	if [ -d "$dir" ]; then
		if [ -f "$dir/backup/relatorio.txt" ]; then
	  	 echo "### Relatório de $dir ###" >> relatorio_final.txt
	 	 cat "$dir/backup/relatorio.txt" >> relatorio_final.txt
	 	 echo "\n\n" >> relatorio_final.txt
		 fi
	fi
done

echo "Relatório final gerado em relatorio_final.txt"
