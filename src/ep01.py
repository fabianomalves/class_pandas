import pandas as pd

# Series
serie_receita = pd.Series(data=[1, 4, 10, 1000, 200, None], name='receita')

# Mostrando a série criada
print(serie_receita)
print(type(serie_receita))

# DataFrame

dados = {'nome': ['Fabiano', 'Moreira', 'Code', 'Ciudad'],
        'sobrenome': ['Moreira', 'Alves', 'Code', 'Del Leste'],
        'idade': [43, 30, 32, 120]}

df_pessoas = pd.DataFrame(dados)

print(df_pessoas)

# Começando a Aula

# Lendo um csv:
path_file_candidatura = '/home/fabiano/Insync/fabiano.moreira.alves@gmail.com/Google Drive/Projects/class_pandas/data/tb_candidatura_2018.csv'
df_candidatura = pd.read_csv(path_file_candidatura, sep=';')
df_candidatura.head()

# Lendo um xlsx:
path_file_declaracao = '/home/fabiano/Insync/fabiano.moreira.alves@gmail.com/Google Drive/Projects/class_pandas/data/tb_declaracao_2018.xlsx'
df_declaracao = pd.read_excel(path_file_declaracao)
df_declaracao.head()

# Brincando com o DataFrame

# Número das primeiras linhas a serem exibidas
df_candidatura.head(2)

# Número das últimas linhas a serem exibidas
df_candidatura.tail(2)

# Descobrindo o número de linhas no DataFrame (tupla), linhas e colunas
df_candidatura.shape

# Quais são as colunas do dataframe? Sabemos que temos 45 colunas
df_candidatura.columns

# Navegando pelas colunas dataframe
df_candidatura['nome']

df_candidatura[['nome', 'cpf', 'descricao_ocupacao']]

colunas_selecionadas = ['nome', 'cpf', 'descricao_ocupacao']

df_candidatura[colunas_selecionadas].head()

# Navegando pelas colunas e linhas do Dataframe
df_candidatura['nome'][29140]  # df[colunm][index]

# Informações do Dataframe
df_candidatura.info()

# Navegando pelas linhas
df_candidatura.iloc[29140:29145]
