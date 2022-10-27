# Tabela Assinatura

insert into assinatura (assinaturaid, assinaturavalor, assinaturaformapagamento, assinaturaplano) values ('4', '19.90', 'Boleto', 'Básico');

select * from assinatura;

# Tabela Cliente

insert into cliente (clienteid, clienteassinatuiraid, clientenome, clientesobrenome, clienteemail, clientesenha)
	values (1, 2, 'David', 'Simas', 'david.simas81@gmail.com', '12345678');

insert into cliente (clienteid, clienteassinatuiraid, clientenome, clientesobrenome, clienteemail, clientesenha)
	values (4, 1, 'Jonas', 'Reiter', 'ana.jonas.reiter@gmail.com', '12345678'),
		   (5, 3, 'Ester', 'Souza', 'ester.souza@gmail.com', '12345678');

select * from cliente;

select clienteid "Código",
	clienteassinatuiraid "Assinatura",
	concat(clientenome , ' ', clientesobrenome) "Nome",
	clienteemail "E-mail",
	assinaturavalor "Valor",
	assinaturaformapagamento "Forma de Pagamento",
	assinaturaplano "Plano"
from cliente
	inner join assinatura on assinaturaid = clienteassinatuiraid;
		
# Tabela Especificações

select * from especificacoes;

insert into especificacoes (especificacoesid, especificacoesidioma, especificacoeslegenda, especificacoesclassificacao, especificacoesanolancamento, especificacoesatores, especificacoesdiretor, especificacoesprodutora)
	values (2,'Português','Inglês','12','15/04/2010','Nicolas Cage','Stanley Kubrick','FOX'),
		   (3,'Português','Frances','16','07/12/2015','Bruce Willis','Howard Hawks','MGM'),
	       (4,'Espanhou','Portugues','18','15/04/2010','Johnny Depp','Spike Lee','Marvell'),
	       (5,'Italiano','Inglês','15','15/04/2010','Tom Cruise','Stanley Kubrick','Walt Disney');
	      
select * from especificacoes;

# Tabela Genero

insert into genero (generoid, generoprincipal)
	values (1,'Ação'),
		   (2,'Ficção','Fantasia'),
	       (3,'Comédia'),
		   (4,'Terror','Violencia'),
		   (5,'Romance');
		  
select * from genero;

# Tabela Filme

insert into filme (filmeid, filmenome, filmeduracao, filmesinopse, filmegeneroid, filmeespecificacoesid)
	values (1,'Mad Max','01:45:30','Um policial muito louco no deserto',1,1),
           (2,'Star Wars','02:15:12','Uma gerra galatica',2,1),
           (3,'Titanic','04:05:46','Um grande navio que naufraga no final',5,3);
          
select * from filme;
          
# Tabela Seriado

insert into seriado (seriadoid, seriadonome, seriadoduracao, seriadosinopse, seriadotemporada, seriadoepisodio, seriadogeneroid, seriadoespecificacoesid)
	values (1,'Os Simpsons','25:00','Histórias reais de uma família amarela',30,15,3,4);

select * from seriado;

# Tabela Historico

insert into historico (historicoid, historicofilmeid, historicoseriadoid, historicoterminou)
	values (1, 1, null, '01/10/2021 10:15:00');

insert into historico (historicoid, historicofilmeid, historicoseriadoid, historicoterminou)
	values (2, null, 1, '27/04/2022 12:15:00');

select * from historico;

# Um busca sobre Cliente

select clienteid "Código",
	clienteassinatuiraid "Assinatura",
    concat(clientenome , ' ', clientesobrenome) "Nome",
	cliente.clienteemail "E-mail",
	filme.filmenome "Título",
	filme.filmesinopse "Sinopse",
	especificacoes.especificacoesidioma "Audio",
	especificacoes.especificacoesclassificacao "Classificação"
from cliente
	inner join historico on historicoid = clientehistoricoid
	inner join filme on filmeid = historicofilmeid
	inner join especificacoes on especificacoesid = filmeespecificacoesid
where clienteid = 1;


		
		
		








