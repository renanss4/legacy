SET SQL_SAFE_UPDATES = 0;
DROP DATABASE IF EXISTS DBCLASSIFICACAO;
CREATE DATABASE DBCLASSIFICACAO;
USE DBCLASSIFICACAO;

CREATE TABLE ALUNO (
	IDALUNO INT NOT NULL PRIMARY KEY AUTO_INCREMENT
	, NOME VARCHAR(45)
	, IDADE INT
);

CREATE TABLE CLASSIFICACAO (	
	CRIANCAS INT
	, JOVENS INT
	, ADULTOS INT
);

INSERT INTO CLASSIFICACAO VALUES (0,0,0);

/*
Regra:
abaixo 10 - Criancas
10 a 18 - Jovens
Acima de 18 - Adulto
*/

DELIMITER $

CREATE TRIGGER TRI_AI_ALUNO AFTER INSERT ON ALUNO FOR EACH ROW
BEGIN
	IF NEW.IDADE < 10 AND NEW.IDADE > 0 THEN
		UPDATE CLASSIFICACAO SET CRIANCAS = CRIANCAS + 1;
    ELSEIF (NEW.IDADE > 10 AND NEW.IDADE < 18) OR (NEW.IDADE = 10 AND NEW.IDADE = 18) THEN
		UPDATE CLASSIFICACAO SET JOVENS = JOVENS + 1;
	ELSEIF NEW.IDADE > 18 THEN
		UPDATE CLASSIFICACAO SET ADULTOS = ADULTOS + 1;
    END IF ;
END $

CREATE TRIGGER TRI_AU_ALUNO AFTER UPDATE ON ALUNO FOR EACH ROW
BEGIN
	IF OLD.IDADE < 10 AND OLD.IDADE > 0 THEN
		UPDATE CLASSIFICACAO SET CRIANCAS = CRIANCAS -1;
	ELSEIF (OLD.IDADE = 10 AND OLD.IDADE = 18) OR (OLD.IDADE > 10 AND OLD.IDADE < 18) THEN
		UPDATE CLASSIFICACAO SET JOVENS = JOVENS -1;
	ELSEIF OLD.IDADE > 18 THEN
		UPDATE CLASSIFICACAO SET ADULTOS = ADULTOS -1;
	END IF ;
        
	IF NEW.IDADE < 10 AND NEW.IDADE > 0 THEN
		UPDATE CLASSIFICACAO SET CRIANCAS = CRIANCAS + 1;
    ELSEIF (NEW.IDADE > 10 AND NEW.IDADE < 18) OR (NEW.IDADE = 10 AND NEW.IDADE = 18) THEN
		UPDATE CLASSIFICACAO SET JOVENS = JOVENS + 1;
	ELSEIF NEW.IDADE > 18 THEN
		UPDATE CLASSIFICACAO SET ADULTOS = ADULTOS + 1;
    END IF ;
END $

CREATE TRIGGER TRI_AD_ALUNO AFTER DELETE ON ALUNO FOR EACH ROW
BEGIN
	IF OLD.IDADE < 10 AND OLD.IDADE > 0 THEN
		UPDATE CLASSIFICACAO SET CRIANCAS = CRIANCAS -1;
	ELSEIF (OLD.IDADE = 10 AND OLD.IDADE = 18) OR (OLD.IDADE > 10 AND OLD.IDADE < 18) THEN
		UPDATE CLASSIFICACAO SET JOVENS = JOVENS -1;
	ELSEIF OLD.IDADE > 18 THEN
		UPDATE CLASSIFICACAO SET ADULTOS = ADULTOS -1;
	END IF ;
END $

CREATE TRIGGER TRI_BI_ALUNO AFTER INSERT ON ALUNO FOR EACH ROW
BEGIN
	-- IF (IFNULL(NEW.IDADE, 0))) IFNULL ALTERA O 1º PARAM PARA O 2º PARAM
	IF (NEW.IDADE < 0 OR NEW.IDADE IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A IDADE É INVÁLIDA!';
	END IF ;
END $

CREATE TRIGGER TRI_BU_ALUNO AFTER UPDATE ON ALUNO FOR EACH ROW
BEGIN
	IF (NEW.IDADE < 0 OR NEW.IDADE IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'A IDADE É INVÁLIDA!';
	END IF ;
END $

DELIMITER ;


INSERT INTO ALUNO(NOME, IDADE) VALUES ('RENAN', 17);
INSERT INTO ALUNO(NOME, IDADE) VALUES ('BIANCA', 8);
INSERT INTO ALUNO(NOME, IDADE) VALUES ('GISELE', 21);

UPDATE ALUNO SET IDADE = 9 WHERE NOME = 'RENAN';
-- UPDATE ALUNO SET IDADE = -1 WHERE NOME = 'GISELE';
DELETE FROM ALUNO WHERE NOME = 'BIANCA'; 

SELECT * FROM ALUNO;
SELECT * FROM CLASSIFICACAO;
SHOW TRIGGERS;