select autor.nome, autor.codAutor, count(livro.cod) as quantidade_publicacoes from autor

join livro on autor.codAutor = livro.autor
group by autor.codAutor, autor.nome

order by quantidade_publicacoes desc
limit 1