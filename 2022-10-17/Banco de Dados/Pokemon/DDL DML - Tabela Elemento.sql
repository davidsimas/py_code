-- DDL --

create table elemento(
    id int generated always as identity primary key,
    tipo VARCHAR(255) not null
);

-- DML --

insert into elemento (tipo)
	values ('Normal'),
		   ('Fighting'),
		   ('Flying'),
		   ('Poison'),
		   ('Ground'),
		   ('Rock'),
		   ('Bug'),
		   ('Ghost'),
		   ('Steel'),
		   ('Fire'),
		   ('Water'),
		   ('Grass'),
		   ('Electric'),
		   ('Psychic'),
		   ('Ice'),
		   ('Dragon'),
		   ('Dark'),
		   ('Fairy');
		   
select * from elemento;