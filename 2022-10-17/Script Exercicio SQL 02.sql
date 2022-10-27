/* fa�a a inser��o de dados em uma tabela de funcionarios esta tabela deve conter no minimo 20 funcion�rios cadastrados
 *  desses 20 funcion�rios 5 devem conter o mesmo sobrenome chamado Lirinha , fa�a uma busca de um filtro em todos os
 *  funcion�rios cadastrados com o nome lirinha ap�s identific� los, realize a altera��o desses sobrenomes para seus respectivos nomes corretos */

insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('David', 'Simas', 11144477735, 1212.35, 29);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Igor', 'Oliveira', 11144477735, 1212.35, 47);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Victor', 'Souza', 11144477735, 1212.35, 41);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Miguel', 'Lirinha', 11144477735, 1212.35, 26);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Bernardo', 'Pereira', 11144477735, 1212.35, 14);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Noah', 'Silva', 11144477735, 1212.35, 9);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Lucas', 'Lirinha', 11144477735, 1212.35, 31);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Samuel', 'Maas', 11144477735, 1212.35, 26);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Pedro', 'Silveira', 11144477735, 1212.35, 46);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Arthur', 'Lourenzo', 11144477735, 1212.35, 53);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Fabiana', 'Wagner', 11144477735, 1212.35, 64);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Jenifer', 'Lirinha', 11144477735, 1212.35, 21);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Breno', 'Santiago', 11144477735, 1212.35, 19);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Maria', 'Lirinha', 11144477735, 1212.35, 22);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Nicole', 'Cordeiro', 11144477735, 1212.35, 47);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Joseane', 'Padilha', 11144477735, 1212.35, 38);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Dominic', 'Lirinha', 11144477735, 1212.35, 16);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Lidiane', 'Silva', 11144477735, 1212.35, 15);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Ferdinand', 'Monteiro', 11144477735, 1212.35, 8);
insert into funcionario (nome, sobrenome, cpf, salario, idade) values ('Vanessa', 'Lobo', 11144477735, 1212.35, 19);

select * from funcionario;

truncate table funcionario;

select * from funcionario where sobrenome = 'Lirinha';

update funcionario set sobrenome = 'Matos' where id = 22;
update funcionario set sobrenome = 'Machado' where id = 25;
update funcionario set sobrenome = 'Saurro' where id = 30;
update funcionario set sobrenome = 'Vaz' where id = 32;
update funcionario set sobrenome = 'Leite' where id = 35;

/* faca uma busca de nomes que cont�m apenas a letra A no inicio do nome utilizando o conceito de de % eliminando os restante da string */

select * from funcionario where nome like 'A%';

/* faca uma busca por filtro de nomes que cont�m apenas a letra A no inicio do nome utilizando utilizando o conceito de % eliminando
 * os restante da string filtre tamb�m se a idade e maior que 18 */

select * from funcionario where nome like 'A%' and idade > 18;

/* apos selecionar todos os nomes que inciam com a letra A, e que sao maior que 18 exclua esses usuarios */

delete from funcionario where nome like 'A%' and idade > 18;

