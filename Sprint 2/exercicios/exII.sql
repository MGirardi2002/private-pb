-- etapa 1
SELECT 
    livro.cod AS CodLivro,
    livro.titulo AS Titulo,
    autor.codautor AS CodAutor,
    autor.nome AS NomeAutor,
    livro.valor AS Valor,
    editora.codeditora AS CodEditora,
    editora.nome AS NomeEditora
FROM 
    livro
JOIN 
    autor ON livro.autor = autor.codautor
JOIN 
    editora ON livro.editora = editora.codeditora
ORDER BY 
    livro.valor DESC
LIMIT 10;

-- etapa 2
SELECT 
    editora.codeditora AS CodEditora,
    editora.nome AS NomeEditora,
    COUNT(livro.cod) AS QuantidadeLivros
FROM 
    livro
JOIN 
    editora ON livro.editora = editora.codeditora
GROUP BY 
    editora.codeditora, editora.nome
ORDER BY 
    QuantidadeLivros DESC
LIMIT 5;