-- DDL -- 

create table people(
	id int generated always as identity,
	nome varchar(45) not null,
	sobrenome varchar(45) not null,
	idade int null
);

select * from people;

alter table people add column cpf varchar(11) not null default '00000000000';

alter table people drop column idade;

alter table people rename to funcionario;

alter table funcionario add column salario decimal(9,2) not null default '0.00';

select * from funcionario;

select
	id as Código,
	nome as Nome,
	sobrenome as Sobrenome
from funcionario;

select * from funcionario where sobrenome like '%va';

insert into funcionario (nome, sobrenome, cpf, salario) values ('João', 'Silva', 11144477735, 1212.35);
insert into funcionario (nome, sobrenome, cpf, salario) values ('Ana', 'Vasconselos', 22255588865, 2212.35);
insert into funcionario (nome, sobrenome, cpf, salario) values ('Alex', 'Saurro', 33344455532, 10000.50);
insert into funcionario (nome, sobrenome, cpf, salario) values ('Joana', 'Gusmão', 43256789654, 500.12), ('Maria', 'Silva', 11133344467, 3455.00);

update funcionario set salario = 3500.00 where id >= 1 and id <= 5;

alter table funcionario add column idade int null;

delete from funcionario where nome like 'João';
delete from funcionario where nome = 'Alex' and sobrenome ='Saurro';
delete from funcionario where salario > 2000;


update funcionario set idade = 16 where id = 10;
update funcionario set idade = 25 where id = 11;
update funcionario set idade = 12 where id = 12;
update funcionario set idade = 36 where id = 13;
update funcionario set idade = 45 where id = 14;
update funcionario set idade = 24 where id = 15;
update funcionario set idade = 18 where id = 16;
update funcionario set idade = 19 where id = 17;
update funcionario set idade = 33 where id = 18;
update funcionario set idade = 29 where id = 19;
update funcionario set idade = 47 where id = 20;
update funcionario set idade = 41 where id = 21;
update funcionario set idade = 26 where id = 22;
update funcionario set idade = 14 where id = 23;
update funcionario set idade = 9 where id = 24;
update funcionario set idade = 31 where id = 25;
update funcionario set idade = 26 where id = 26;
update funcionario set idade = 46 where id = 27;
update funcionario set idade = 53 where id = 28;
update funcionario set idade = 64 where id = 29;
update funcionario set idade = 21 where id = 30;
update funcionario set idade = 19 where id = 31;
update funcionario set idade = 22 where id = 32;
update funcionario set idade = 47 where id = 33;
update funcionario set idade = 38 where id = 34;
update funcionario set idade = 16 where id = 35;
update funcionario set idade = 15 where id = 36;
update funcionario set idade = 8 where id = 37;
update funcionario set idade = 19 where id = 38;



