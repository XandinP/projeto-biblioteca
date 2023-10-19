ALTER TABLE EMPRESTIMO DROP CONSTRAINT ALUNO_EMPRESTIMO_FK;
ALTER TABLE EMPRESTIMO DROP CONSTRAINT ALUNO_EMPRESTIMO_FK;


DROP TABLE EMPRESTIMO;
DROP TABLE ALUNO;
DROP TABLE LIVRO;



DROP SEQUENCE EMPRESTIMO_IDEMPRESTIMO_SEQ;
DROP SEQUENCE ALUNO_NUMID_SEQ;

CREATE TABLE LIVRO (
                ISBN VARCHAR2(13) NOT NULL,
                TITULO VARCHAR2(255) NOT NULL,
                AUTOR VARCHAR2(100) NOT NULL,
                ANO NUMBER NOT NULL,
                CATEGORIA VARCHAR2(50),
                NUMCOPIASDISPONIVEIS NUMBER NOT NULL,
                CONSTRAINT LIVRO_PK PRIMARY KEY (ISBN)
);

CREATE TABLE ALUNO (
                NUMID NUMBER NOT NULL,
                TURMA VARCHAR2(10) NOT NULL,
                NOME VARCHAR2(100) NOT NULL,
                CONSTRAINT ALUNO_PK PRIMARY KEY (NUMID)
);

CREATE TABLE EMPRESTIMO (
                IDEMPRESTIMO NUMBER NOT NULL,
                DATAEMPRESTIMO DATE NOT NULL,
                DATADEVOLUCAO DATE,
                ISBN VARCHAR2(13) NOT NULL,
                NUMID NUMBER NOT NULL,
                CONSTRAINT EMPRESTIMO_PK PRIMARY KEY (IDEMPRESTIMO)
);

CREATE SEQUENCE EMPRESTIMO_IDEMPRESTIMO_SEQ;
CREATE SEQUENCE ALUNO_NUMID_SEQ;


ALTER TABLE EMPRESTIMO ADD CONSTRAINT ALUNO_EMPRESTIMO_FK
FOREIGN KEY (NUMID)
REFERENCES ALUNO (NUMID)
NOT DEFERRABLE;

ALTER TABLE EMPRESTIMO ADD CONSTRAINT LIVRO_EMPRESTIMO_FK
FOREIGN KEY (ISBN)
REFERENCES LIVRO (ISBN)
NOT DEFERRABLE;


GRANT ALL ON EMPRESTIMO TO 
GRANT ALL ON ALUNO TO 
GRANT ALL ON LIVRO TO 


ALTER USER quota unlimited on USERS;