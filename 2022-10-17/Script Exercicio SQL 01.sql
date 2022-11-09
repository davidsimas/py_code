/* Crie uma tabela com nome de sua prefer�ncia crie um id imut�vel crie atributos de nome sobrenome sal�rio e idade. 
 * altere essa tabela adicione uma coluna de cpf crie uma tabela de animais adicione no minimo 5 caracter�sticas
 * desses animais apenas o conceito de colunas crie uma tabela livros adicione 5 conceitos que um livro contem , 
 * depois altere essa tabela e adicione uma coluna ISBN delete a tabela animais delete a tabela livros crie 3 tabelas
 * utilizando o conceito de id by default essas tabelas podem ser de sua vontade
 */


create table empresax (
	nome varchar(45) not null,
	sobrenome varchar(45) not null,
	idade integer null
);


INSERT INTO empresax (nome, sobrenome, idade) VALUES ('David', 'Simas', 41);
INSERT INTO empresax (nome, sobrenome, idade) VALUES ('Marcio', 'Louren�o', 27);
INSERT INTO empresax (nome, sobrenome, idade) VALUES ('Maria', 'Gabriela', 21);

select * from empresax;

ALTER TABLE empresax ADD COLUMN cpf varchar(11) not null default '00000000000';

ALTER TABLE empresax DROP COLUMN cpf;


/* Gerarando um id imult�vel e mut�vel
 * generated by default as identity - Permiti inser��o de dados 
 * generated always as identity - ID imult�vel
 */

alter table empresax add cpf bigint not null;

/* Deletar uma coluna
 * ALTER TABLE nome_tabela DROP COLUMN nome_coluna;
 */

ALTER TABLE empresax DROP COLUMN idade;
alter table carro 

create table aminais (
	id int not null generated by default as identity,
	especie varchar(25),
	cor varchar(15),
	quantidadePatas int,
	cola boolean,
	peso int
);

create table livro (
	id int not null generated by default as identity,
	titulo varchar(45),
	autor varchar(45),
	editora varchar(45),
	lancamento date,
	genero varchar(15)		
);

alter table livro add isbn bigint not null;

drop table aminais;

drop table livro;

CREATE TABLE carro (
	id int NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	marca varchar(45) NULL,
	modelo varchar(25) NULL,
	cor varchar(15) NULL,
	ano date NULL
);

create table aluno (
	id int NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	nome varchar(45),
	nomePai varchar(45),
	nomeMae varchar(45),
	escola varchar(50),
	turno varchar(10),
	dataNasc date
);

create table cerveja (
	id int NOT NULL GENERATED BY DEFAULT AS IDENTITY,
	fabricante varchar(45),
	estilo varchar(30),
	abv decimal(2,1),
	ibu int
);