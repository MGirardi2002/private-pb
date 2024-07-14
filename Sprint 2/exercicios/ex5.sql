select distinct autor.nome

from autor

INNER join livro on autor.codAutor = livro.autor 
INNER join editora on livro.editora = editora.codEditora
inner join endereco on editora.endereco = endereco.codEndereco

where endereco.estado NOT IN ('PARANÁ','SANTA CATARINA','RIO GRANDE DO SUL')
order by autor.nome