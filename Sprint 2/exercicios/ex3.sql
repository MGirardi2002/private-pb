SELECT
	count(*) as quantidade, e.nome, en.estado, en.cidade
FROM
	editora e
INNER JOIN livro l ON e.codeditora = l.editora
INNER JOIN endereco en ON e.endereco = en.codendereco
GROUP BY e.codeditora 
ORDER BY quantidade desc
LIMIT 5