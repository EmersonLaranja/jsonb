\connect "postgres";

DROP TABLE IF EXISTS "produtos";

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    descricao TEXT,
    preco DECIMAL(10, 2),
    detalhes JSON
);
