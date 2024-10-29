-- professores

CREATE TABLE professores (
 matricula INTEGER PRIMARY KEY,
  nome_professor TEXT NOT NULL,
  genero TEXT NOT NULL
);

-- injeção de dados-teste
INSERT INTO professores VALUES (1, 'Marlene', 'F');
INSERT INTO professores VALUES (2, 'Joelson', 'M');


-- consultando as injeções realizadas
SELECT * FROM professores WHERE matricula=1