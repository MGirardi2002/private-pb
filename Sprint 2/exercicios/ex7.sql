SELECT autor.nome FROM autor 
left JOIN livro ON autor.codautor = livro.autor 

GROUP BY autor.codautor, AUTOR.nome
HAVING count(livro.cod) = 0