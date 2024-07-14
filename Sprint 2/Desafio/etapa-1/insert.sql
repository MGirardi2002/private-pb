INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao
WHERE idVendedor NOT IN (SELECT idVendedor FROM Vendedor);

INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao
WHERE idCombustivel NOT IN (SELECT idCombustivel FROM Combustivel);

INSERT INTO Carro (idCarro, kmCarro, marcaCarro, anoCarro, modeloCarro, classiCarro, idCombustivel)
SELECT idCarro, kmCarro, marcaCarro, anoCarro, modeloCarro, classiCarro, idCombustivel
FROM (
    SELECT idCarro, kmCarro, marcaCarro, anoCarro, modeloCarro, classiCarro, idCombustivel,
           ROW_NUMBER() OVER (PARTITION BY idCarro ORDER BY idCarro) as rn
    FROM tb_locacao
) sub
WHERE rn = 1;

INSERT INTO Cliente (idCliente, nomeCliente)
SELECT DISTINCT idCliente, nomeCliente
FROM tb_locacao 
WHERE idCliente NOT IN (SELECT idCliente FROM Cliente);

INSERT INTO Endereco (idCliente, paisCliente, estadoCliente, cidadeCliente)
SELECT DISTINCT idCliente, paisCliente ,estadoCliente ,cidadeCliente 
FROM tb_locacao 
WHERE idCliente NOT IN (SELECT idCliente FROM Endereco);

INSERT INTO Locacao (idLocacao, idCliente, idVendedor, idCarro, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria)
SELECT idLocacao, idCliente, idVendedor, idCarro, dataLocacao, horaLocacao, dataEntrega, horaEntrega, qtdDiaria, vlrDiaria
FROM tb_locacao
WHERE idLocacao NOT IN (SELECT idLocacao FROM Locacao);