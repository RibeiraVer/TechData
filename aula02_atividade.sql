--Crie mais duas tabelas (sugestão: 'cursos' e 'filiais') no mesmo banco de dados
--onde você criou 'alunos' e 'professores'. Façam mais características para essas tabelas (ao menos 5)
--e criem, pelo menos, 10 injeções de dados para as novas tabelas e 1 consulta para cada uma delas. 
--No final, peça (no VSCode) para que o Pandas leia cada tabela nova que foi criada.

--Dados para a tabela cursos

--CURSO
INSERT INTO cursos (id_curso, nome, duracao, nivel, preco, descricao, data_inicio, id_professor) VALUES
(1, 'Curso de Python', 6, 'Intermediário', 1200.00, 'Aprenda Python do zero a um nível avançado.', '2024-01-15', 1),
(2, 'Curso de Data Science', 12, 'Avançado', 2500.00, 'Formação completa em ciência de dados.', '2024-02-01', 2),
(3, 'Curso de Web Development', 8, 'Básico', 1500.00, 'Introdução ao desenvolvimento web.', '2024-03-10', 3),
(4, 'Curso de Machine Learning', 10, 'Avançado', 2000.00, 'Aprenda algoritmos de aprendizado de máquina.', '2024-04-05', 2),
(5, 'Curso de Excel', 3, 'Básico', 800.00, 'Domine as funções do Excel para o mercado de trabalho.', '2024-01-20', 1),
(6, 'Curso de Design Gráfico', 4, 'Intermediário', 1800.00, 'Criação de peças gráficas para diferentes mídias.', '2024-05-01', 3),
(7, 'Curso de Marketing Digital', 5, 'Intermediário', 1400.00, 'Estratégias de marketing para o ambiente digital.', '2024-06-15', 1),
(8, 'Curso de Desenvolvimento Mobile', 7, 'Intermediário', 1900.00, 'Criação de aplicativos para Android e iOS.', '2024-07-01', 3),
(9, 'Curso de Segurança da Informação', 6, 'Avançado', 2200.00, 'Fundamentos e práticas de segurança cibernética.', '2024-08-10', 2),
(10, 'Curso de Inteligência Artificial', 11, 'Avançado', 3000.00, 'Conceitos e aplicações de IA no mundo real.', '2024-09-05', 2);


--FILIAIS
INSERT INTO filiais (id_filial, nome, endereco, telefone, cidade, estado, email, capacidade) VALUES
(1, 'Filial Centro', 'Rua A, 123', '(11) 1234-5678', 'São Paulo', 'SP', 'centro@escola.com', 100),
(2, 'Filial Zona Sul', 'Avenida B, 456', '(11) 9876-5432', 'São Paulo', 'SP', 'zonasul@escola.com', 80),
(3, 'Filial Zona Norte', 'Rua C, 789', '(11) 2345-6789', 'São Paulo', 'SP', 'zonanorte@escola.com', 60),
(4, 'Filial Barra', 'Rua D, 101', '(21) 3210-9876', 'Rio de Janeiro', 'RJ', 'barra@escola.com', 70),
(5, 'Filial Ipanema', 'Avenida E, 202', '(21) 6543-2109', 'Rio de Janeiro', 'RJ', 'ipanema@escola.com', 90),
(6, 'Filial Curitiba', 'Rua F, 303', '(41) 8765-4321', 'Curitiba', 'PR', 'curitiba@escola.com', 50),
(7, 'Filial Belo Horizonte', 'Avenida G, 404', '(31) 4321-8765', 'Belo Horizonte', 'MG', 'bh@escola.com', 75),
(8, 'Filial Porto Alegre', 'Rua H, 505', '(51) 5678-1234', 'Porto Alegre', 'RS', 'poa@escola.com', 65),
(9, 'Filial Brasília', 'Avenida I, 606', '(61) 6789-2345', 'Brasília', 'DF', 'brasilia@escola.com', 85),
(10, 'Filial Salvador', 'Rua J, 707', '(71) 7890-3456', 'Salvador', 'BA', 'salvador@escola.com', 100);


--consulta pela tabela do curso
SELECT * FROM cursos WHERE nivel = 'Avançado';

--consulta pela tabela filiais
SELECT * FROM filiais WHERE capacidade > 70;

--Ler Tabelas com Pandas no VSCode
import pandas as pd
import sqlite3  # ou o conector apropriado para seu banco de dados

# Conectar ao banco de dados
conn = sqlite3.connect('seu_banco_de_dados.db')

# Ler as tabelas
cursos_df = pd.read_sql_query("SELECT * FROM cursos", conn)
filiais_df = pd.read_sql_query("SELECT * FROM filiais", conn)

# Fechar a conexão
conn.close()

# Exibir os DataFrames
print(cursos_df)
print(filiais_df)

