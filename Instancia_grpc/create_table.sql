CREATE TABLE DadosSensores (
	id BIGINT NOT NULL AUTO_INCREMENT,
	data DATETIME NOT NULL,
	id_sensor INT NOT NULL,
	localizacao VARCHAR(30) NOT NULL,
	valor FLOAT NOT NULL,
	PRIMARY KEY (id)
);