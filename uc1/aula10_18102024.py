# Pandas (pandas.pydata.org)
#
import pandas as pd #(pd=alias)
print(pd.__version__)

#CRIAÇÃO DE UM DATASET:

data = {'Cargo': ['Analista', 'Gerente', 'Estagiário'],
        'Salário': [4500, 9000, 2000]}
cargos_salarios = pd.DataFrame(data)
print(cargos_salarios)

#CRIAÇÃO DE UMA SÉRIE:

cargos = pd.Series(['Analista', 'Gerente', 'Estagiário'], index=[1, 2, 3])
print(cargos)

#ATIVIDADE ASSISTIDA:

#Crie um dataset de 3 colunas com as seguintes informações: 'nome de um filme', 'ano de lançamento' e 'gênero'.

#Resolução:
import pandas as pd

data_cinema={'Título':['Cidade de Deus','Divertidamente 2','Uma Linda Mulher'],
        'Ano de Lançamento':[2002, 2024, 1990],
        'Gênero':['Drama', 'Animação','Romance']
}
cinema=pd.DataFrame(data_cinema)
print(cinema)

#ACESSO À DATASETS EXTERNOS:

#https://www.kaggle.com/datasets/thebumpkin/700-classic-disco-tracks-with-spotify-data

df_disco = pd.read_csv('path_to_dataset.csv')
print(df_disco.head())  # Exibe as primeiras linhas
print(df_disco.tail())  # Exibe as cinco últimas linhas

#Leitura de Arquivos e Filtragem:

to_string(): #Exibe o DataFrame completo como uma string, útil para visualização.

pd.set_option('display.max_rows',3)  #Define o número máximo de linhas a ser exibido.

Filtragem de Dados: #Exemplo de filtragem por colunas e linhas específicas:

df_filtrado = df_disco[df_disco['Artista'] == 'Bee Gees']
print(df_filtrado)

#Criação de Novas Colunas: adicionar colunas derivadas

df_disco['Duração_Minutos'] = df_disco['Duração_Segundos'] / 60

#Leitura de Arquivos Excel e Outros Formatos:
df_disco_2 = pd.read_excel('seuarquivo.xlsx')
df_disco_3 = pd.read_json('seuarquivo.json')
df_disco_4 = pd.read_html('seuarquivo.html')
df_disco_5 = pd.read_sql('seuarquivo.sql')


#Atividade Prática:
#
#Através do Kaggle, procurem outros datasets e apliquem os comandos trabalhados anteriormente.

