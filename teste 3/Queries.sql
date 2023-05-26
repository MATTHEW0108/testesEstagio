use testes;

SET GLOBAL local_infile=1;

CREATE TABLE ans (
	rAns varchar (10),
    cnpj varchar(20),
    razSoc varchar (150),
    nomFan varchar (100),
	modal varchar (50),
    logr varchar (100),
    num varchar (50),
    compl varchar (100),
    bairro varchar (50),
    cidade varchar (50),
    uf varchar(5),
    cep varchar(10),
    ddd varchar(10),
    telefone varchar(20),
    fax varchar(15),
    endEl varchar(50),
    represent varchar (60),
    cargoR varchar (60),
    dataReg varchar (25),
    primary key (rAns)
);


create table conj_dados (
	org varchar (60),
    nome varchar (75),
    descr varchar (500),
    tags varchar (300),
    qtdRec int,
    qtdReu int, 
    qtdDownl int,
    qtdSeg int
);

show variables like "secure_file_priv";

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Relatorio_cadop.csv' into table ans CHARACTER SET latin1 fields terminated by ';' enclosed by '' lines terminated by '\n'ignore 1 rows ;

select * from  ans