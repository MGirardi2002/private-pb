CREATE VIEW dim_Cliente AS
SELECT
    l.idLocacao,
    c.idCliente,
    c.nomeCliente,
    e.paisCliente,
    e.estadoCliente,
    e.cidadeCliente
FROM
    Locacao l
JOIN
    Cliente c ON l.idCliente = c.idCliente
JOIN
    Endereco e ON l.idCliente = e.idCliente;
   
CREATE VIEW dim_Tempo AS
SELECT
    l.idLocacao,
    l.dataLocacao,
    l.horaLocacao,
    l.dataEntrega,
    l.horaEntrega
FROM
    Locacao l;
   
   CREATE VIEW fato_Locacao AS
SELECT
    l.idLocacao,
    l.idCliente,
    l.idVendedor,
    l.idCarro,
    car.idCombustivel,
    l.qtdDiaria,
    l.vlrDiaria,
    l.kmCombustivel
FROM
    Locacao l
JOIN
    Carro car ON l.idCarro = car.idCarro;
   
CREATE VIEW dim_Carro AS
SELECT
    l.idLocacao,
    car.idCarro,
    car.kmCarro,
    car.marcaCarro,
    car.anoCarro,
    car.modeloCarro,
    car.classiCarro,
    car.idCombustivel
FROM
    Locacao l
JOIN
    Carro car ON l.idCarro = car.idCarro
JOIN
    Combustivel comb ON car.idCombustivel = comb.idCombustivel;
   
CREATE VIEW dim_Vendedor AS
SELECT
    l.idLocacao,
    v.idVendedor,
    v.nomeVendedor,
    v.sexoVendedor,
    v.estadoVendedor
FROM
    Locacao l
JOIN
    Vendedor v ON l.idVendedor = v.idVendedor;

CREATE VIEW dim_Combustivel AS
SELECT
    car.idCarro,
    comb.idCombustivel,
    comb.tipoCombustivel
FROM
    Carro car
JOIN
    Combustivel comb ON car.idCombustivel = comb.idCombustivel;