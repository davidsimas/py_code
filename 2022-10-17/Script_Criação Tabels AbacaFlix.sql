-- DDL -- 

create table clientes(
    cliente_id integer not null,
    nome varchar(255) not null,
    sobrenome varchar(255) not null,
    email varchar(255) not null,
    senha varchar(20) not null,
    fk_assinatura integer not null,
    primary key (cliente_id)
);

create table assinatura(
	assinatura_id integer not null,
	valor decimal(5,2) not null,
	forma_pagamento varchar(20) not null,
	plano varchar(20) not null,
	primary key (assinatura_id)
);

alter table clientes
	add constraint cliente_assinatura
	foreign key(fk_assinatura)
	references assinatura(assinatura_id);

create table historico(
	historico_id integer not null,
	andamento varchar(50),
	terminou varchar(50),
	fk_clientes integer not null,
	fk_filmes integer not null,
	fk_series integer not null,
	primary key (historico_id)
);

alter table historico
	add constraint cliente_historico
	foreign key(fk_clientes)
	references clientes(cliente_id);

create table filmes(
	filmes_id integer not null,
	titulo varchar(100),
	duracao time(0) not null,
	sinopse varchar(255) not null,
	fk_especificacoes integer not null,
	primary key (filmes_id)
);

create table series(
	series_id integer not null,
	titulo varchar(100) not null,
	temporadas integer not null,
	episodios integer not null,
	duracao time(0) not null,
	sinopse varchar(255) not null,
	fk_especificacoes integer not null,
	primary key (series_id)
);

alter table historico
	add constraint historico_filme
	foreign key(fk_filmes)
	references filmes(filmes_id);

alter table historico
	add constraint historico_series
	foreign key(fk_series)	            
	references series(series_id);

create table especificacoes(
	especificacoes_id integer not null,
	idioma varchar(20) not null,
	legenda varchar(20) not null,
	classificacao integer not null,
	genero varchar(20) not null,
	ano_lancamento date not null,
	audio varchar(20) not null,
	atores varchar(255) not null,
	diretor varchar(100) not null,
	produtora varchar(100) not null,
	primary key (especificacoes_id)
);

alter table filmes
	add constraint filme_especificacoes
	foreign key(fk_especificacoes)	            
	references especificacoes(especificacoes_id);

alter table series
	add constraint serie_especificacoes
	foreign key(fk_especificacoes)	            
	references especificacoes(especificacoes_id);



























