import pandas as pd
br_feriados = pd.read_csv('feriados.csv', on_bad_lives='skip')
print(br_feriados.head())  # Exibe as primeiras linhas
print(br_feriados.tail())  # Exibe as cinco últimas linhas

from sqlalchemy import create_engine


