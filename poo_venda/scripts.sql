CREATE DATABASE loja;

USE loja;

CREATE TABLE categorias (
    id_categoria INT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE produtos (
    id_produto INT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10, 2),
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria)
);

CREATE TABLE vendas (
    id_venda INT PRIMARY KEY,
    total DECIMAL(10, 2),
    data_venda DATE
);
