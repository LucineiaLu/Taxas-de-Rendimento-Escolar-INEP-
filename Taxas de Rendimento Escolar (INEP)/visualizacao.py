import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Carregar o dataset
df = pd.read_csv('Taxas_de_Rendimento_Escolar_2013_2023.csv')

# Filtrar os dados para o ano de 2023 e região Sudeste
df_sudeste = df[(df['Ano'] == 2023) & (df['Região'] == 'Sudeste')]

# Filtrar para os estados de Minas Gerais, São Paulo e Rio de Janeiro
df_final = df_sudeste[df_sudeste['Estado'].isin(['Minas Gerais', 'São Paulo', 'Rio de Janeiro'])]

# Exibir as primeiras linhas do dataframe
print(df_final.head())
