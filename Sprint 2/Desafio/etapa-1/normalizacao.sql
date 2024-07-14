create table Vendedor (
	idVendedor INTEGER primary key,
	nomeVendedor VARCHAR(50),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR(50)
);

create table Carro (
	idCarro Integer primary key,
	kmCarro INTEGER,
	marcaCarro VARCHAR(50),
	anoCarro INTEGER,
	modeloCarro VARCHAR(50),
	classiCarro VARCHAR(50),
	idCombustivel INTEGER,
	 FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
);

create table Combustivel (
	idCombustivel INTEGER primary key,
	tipoCombustivel
);

create table Locacao (
	idLocacao INTEGER PRIMARY KEY,
	idCliente INTEGER,
	idVendedor INTEGER,
	idCarro INTEGER,
	dataLocacao DATE,
	horaLocacao TIME,
	dataEntrega DATE,
	horaEntrega TIME,
	qtdDiaria INTEGER,
	vlrDiaria DECIMAL,
	kmCombustivel INTEGER,
	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro)
);

create table Cliente (
	idCliente INTEGER PRIMARY KEY,
	nomeCliente VARCHAR(50)
);

create table Endereco (
	idCliente INTEGER,
	paisCliente VARCHAR(50),
	estadoCliente VARCHAR(50),
	cidadeCliente VARCHAR(50),
	FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente)
);


