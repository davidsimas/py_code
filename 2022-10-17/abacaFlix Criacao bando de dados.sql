create table cliente (
    clienteId integer not null,
    clienteAssinatuiraId integer null,
    clienteHistoricoId integer null, 
    clienteNome varchar(50) not null,
    clienteSobreNome varchar(50) not null,
    clienteEmail varchar(50) not null,
    clienteSenha varchar(50) not null,
    primary key (clienteId)
);

create table assinatura (
    assinaturaId integer not null, 
    assinaturaValor decimal(5,2) not null,
    assinaturaFormaPagamento varchar(50) not null,
    assinaturaPlano varchar(50) not null,
    primary key (assinaturaId)
);

alter table cliente 
    add constraint cliente_assinaturaId 
    foreign key(clienteAssinatuiraId) references assinatura(assinaturaId);

create table historico (
    historicoId integer not null,
    historicoFilmeId integer not null,
    HistoricoSeriadoId integer not null, 
    historicoterminou varchar(50) not null,
    historicoandamento varchar(50) not null,
    historicominhalista varchar(50) not null,
    primary key (historicoId)
);

alter table cliente 
    add constraint cliente_historicoId 
    foreign key(clienteHistoricoId) references historico(historicoId);

create table filme (
    filmeId integer not null,
    filmeNome varchar(50) not null,
    filmeDuracao time(0) without time zone not null,
    filmeSinopse varchar(255) not null,
    filmeGeneroId integer not null,
    filmeEspecificacoesId integer not null,
    primary key (filmeId)
);

create table seriado (
    seriadoId integer not null,
    seriadoNome varchar(50) not null,
    seriadoDuracao time(0) without time zone not null,
    seriadoSinopse varchar(255) not null,
    seriadoTemporada integer not null,
    seriadoEpisodio integer not null,
    seriadoGeneroId integer not null,
    seriadoEspecificacoesId integer not null,
    primary key (seriadoId)
);

alter table historico 
    add constraint historicoFilmeId_filmeId 
    foreign key(historicoFilmeId) references filme(filmeId);

alter table historico 
    add constraint HistoricoSeriadoId_seriadoId 
    foreign key(HistoricoSeriadoId) references seriado(seriadoId);

create table genero (
    generoId integer not null, 
    generoPrincipal varchar(50) not null,
    generoSecundario varchar(50) null,
    primary key (generoId)
);

alter table filme 
    add constraint filmeGeneroId_generoId 
    foreign key(filmeGeneroId) references genero(generoId);

alter table seriado 
    add constraint seriadoGeneroId_generoId 
    foreign key(seriadoGeneroId) references genero(generoId);

create table especificacoes (
    especificacoesId integer not null, 
    especificacoesIdioma varchar(50) not null,
    especificacoesLegenda varchar(50) not null,
    especificacoesClassificacao varchar(50) not null,
    especificacoesAnoLancamento varchar(50) not null,
    especificacoesAudio varchar(50) not null,
    especificacoesAtores varchar(50) not null,
    especificacoesDiretor varchar(50) not null,
    especificacoesProdutora varchar(50) not null,
    primary key (especificacoesId)
);

alter table filme 
    add constraint filmeEspecificacoesId_especificacoesId 
    foreign key(filmeEspecificacoesId) references especificacoes(especificacoesId);

alter table seriado 
    add constraint seriadoEspecificacoesId_especificacoesId
    foreign key(seriadoEspecificacoesId) references especificacoes(especificacoesId);

commit;