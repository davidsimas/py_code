-- DDL -- 

create table people(
	id int generated always as identity,
	nome varchar(45) not null,
	sobrenome varchar(45) not null,
	idade int null
);

-- DML --

select * from people;

INSERT INTO people (nome, sobrenome, idade) VALUES ('Pedro', 'Ferreira', 18), ('João', 'Pereira', 50);
INSERT INTO people (nome, sobrenome, idade) VALUES ('David', 'Simas', 41);
INSERT INTO people (nome, sobrenome, idade) VALUES ('Marcio', 'Lourenço', 27);
INSERT INTO people (nome, sobrenome, idade) VALUES ('Maria', 'Gabriela', 21);

UPDATE people SET idade = 42 WHERE id = 2;

update people set sobrenome = 'Abacate' where id >=2 and id <=4;

delete from people where id = 2;

delete from people where nome = 'Marcio';
