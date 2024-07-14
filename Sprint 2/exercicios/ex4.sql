select  nome, codAutor, nascimento, COUNT(livro.cod) as quantidade 
from autor 	
left join livro on autor.codautor = livro.autor 
group by autor.codautor, autor.nome ,autor.nascimento 
order by autor.nome