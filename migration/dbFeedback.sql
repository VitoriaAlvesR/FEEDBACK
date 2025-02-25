-- Criação de uma database
CREATE DATABASE db_feedback;

-- Usando a database
USE db_feedback;

-- Criação de uma tabela com orientações necessárias para a continuidade do projeto
CREATE TABLE tb_comentarios (
nome VARCHAR (150) NOT NULL, 
cod_comentario INT AUTO_INCREMENT PRIMARY KEY,
comentario TEXT NOT NULL,
dataehora_comentario DATETIME NOT NULL
);


