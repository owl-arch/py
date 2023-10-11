import pandas as pd
import matplotlib as plt
from tqdm import tqdm

# Library de tratamento de codificação de caracteres (pip3 install unidecode)
import unidecode
import unicodedata

# pd.options.display.max_rows = 200

file_input = 'ibge/tab_4714_pop_2022_brasil_importar_QGIS.csv'

with tqdm(desc="Load CSV to DataFrame") as bar:
    # não pula nenhuma das linhas, mas atualize a barra de progresso
    df = pd.read_csv(file_input,
                     delimiter=';',
                     index_col=0,
                     encoding='ISO-8859-1',
                     skiprows=lambda x: bar.update(1) and False
                     )
# print(df.columns.values)
# print(df.dtypes)

print("Sanitização da UF")

df['UF'] = df['Municipio'].str.extract('(\([a-zA-Z]{2}\))')
df['UF'] = df['UF'].str.slice(start=1, stop=-1)

print("Sanitização do Municipio")

tqdm.pandas(desc="Sanitizando: Municipio")
df['Municipio'] = df['Municipio'].str.slice(
    start=0, stop=-5)

# df['NFC'] = df['Municipio'].str.normalize('NFC')

table_portugues = str.maketrans({'á': 'a', 'à': 'a', 'â': 'a',
                                 'é': 'e', 'ê': 'e',
                                 'ó': 'o', 'ô': 'o',
                                 'ú': 'u', 'ü': 'u',
                                 'í': 'i',
                                 'ç': 'c'})

df['Municipio'] = df['Municipio'].str.translate(table_portugues)
df['Municipio'] = df['Municipio'].str.upper()

df['Municipio'] = df['Municipio'].str.upper()

print("\nDataframe:")
print(df)

ibge_output = 'dataset/ibge_2022_mun.csv'
print(f"🔹 Gravando  {ibge_output}")
df.to_csv(ibge_output, index=False, sep=';')
