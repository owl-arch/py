import pandas as pd
from tqdm import tqdm

pd.options.display.float_format = "{:.2f}".format  # Formato float
# pd.options.display.max_rows = 200                  # Max de linhas a listar
# print(pd.options.display.max_rows)

# colunas_selecionadas_bolsa_familia = ['UF', 'NOME MUNICÍPIO', 'CPF FAVORECIDO',
#                                      'NIS FAVORECIDO', 'NOME FAVORECIDO',
#                                      'VALOR PARCELA']


# encoding 'latin-1' é o mesmo que 'ISO-8859-1'

##
# IBGE - Censo da População em 2022
##
file_input = './social/202306_NovoBolsaFamilia.csv'

print("")
print(f"🎯 SOCIAL - Novo Bolsa Familia = {file_input}")
with tqdm(desc="☁️ Carregando arquivo CSV") as bar:
    # não pula nenhuma das linhas, mas
    # atualize a barra de progresso
    df = pd.read_csv(file_input,
                     delimiter=';',
                     encoding='ISO-8859-1',
                     # nrows=2000000,
                     usecols=['UF', 'NOME MUNICÍPIO',
                              'NOME FAVORECIDO', 'VALOR PARCELA'],
                     skiprows=lambda x: bar.update(1) and False
                     )

# print('\n')
print('📌 Ajustes nos dados carregados')
# df.columns = ['UF', 'Municipio', 'CPF', 'NIS', 'Nome', 'Valor']
df.columns = ['UF', 'Municipio', 'Nome', 'Valor']

tqdm.pandas(desc="  🔹 Removendo decimais     ")
df['Valor'] = df['Valor'].str.replace(',00', '').progress_apply(lambda x: x)

tqdm.pandas(desc="  🔹 Transformando em 'int' ")
df['Valor'] = df['Valor'].astype(int).progress_apply(lambda x: x)

##
# IBGE - Censo da População em 2022
##
file_input = 'dataset/ibge_2022_mun.csv'

print("")
print(f"🎯 IBGE - População no Censo 2022 = {file_input}")
with tqdm(desc="☁️ Carregando arquivo CSV") as bar:
    # não pula nenhuma das linhas, mas atualize a barra de progresso
    df_ibge = pd.read_csv(file_input,
                          delimiter=';',
                          index_col=[0, 2],
                          encoding='ISO-8859-1',
                          usecols=['Municipio', 'UF', 'pop_2022',],
                          skiprows=lambda x: bar.update(1) and False
                          )

print("\n")

print(df_ibge)

##
# Processamento dos Municípios
##


def municipio():
    print("📌 Municipios")

    # Cálculos
    tqdm.pandas(desc="🔹 Total ")
    municipio = df.groupby(['Municipio', 'UF'])[
        'Valor'].sum().progress_apply(lambda x: x)
    municipio = pd.DataFrame(municipio)

    tqdm.pandas(desc="🔹 count ")
    municipio['count'] = df.groupby(
        ['Municipio', 'UF'])['Valor'].count().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 mean  ")
    municipio['mean'] = df.groupby(
        ['Municipio', 'UF'])['Valor'].mean().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 std   ")
    municipio['std'] = df.groupby(
        ['Municipio', 'UF'])['Valor'].std().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 min   ")
    municipio['min'] = df.groupby(
        ['Municipio', 'UF'])['Valor'].min().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹  1%   ")
    municipio['1%'] = df.groupby(['Municipio', 'UF'])['Valor'].quantile(
        q=0.01).progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 50%   ")
    municipio['50%'] = df.groupby(['Municipio', 'UF'])['Valor'].quantile(
        q=0.50).progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 99%   ")
    municipio['99%'] = df.groupby(['Municipio', 'UF'])['Valor'].quantile(
        q=0.99).progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 max   ")
    municipio['max'] = df.groupby(
        ['Municipio', 'UF'])['Valor'].max().progress_apply(lambda x: x)

    # Ajustes na estatistica descritiva dos recursos do Município
    municipio['count'] = municipio['count'].astype(int)
    municipio['min'] = municipio['min'].astype(int)
    municipio['1%'] = municipio['1%'].astype(int)
    municipio['50%'] = municipio['50%'].astype(int)
    municipio['99%'] = municipio['99%'].astype(int)
    municipio['max'] = municipio['max'].astype(int)
    municipio.columns = ['Recursos', 'Beneficiarios', 'Media', 'Desvio',
                         'Minimo', 'Perc_1', 'Mediana', 'Perc_99', 'Maximo']

    print(municipio)

    tqdm.pandas(desc="🔹 Merge ")
    # Merge
    # Método de mesclagem - Descrição
    # -----------------------------------------------------------------
    # left - Use as teclas apenas do quadro esquerdo
    # right - Use chaves apenas do quadro direito
    # outer - Use união de chaves de ambos os frames
    # inner - Use a interseção de chaves de ambos os quadros
    # cross - Crie o produto cartesiano das linhas de ambos os quadros
    municipio = pd.merge(municipio, df_ibge, on=[
                         "Municipio", "UF"], how='right').progress_apply(lambda x: x)

    # municipio = pd.merge(municipio, df_ibge,
    #                     right_index=True,
    #                     left_index=True).progress_apply(lambda x: x)

    # Cálcula Percentual utilizado pela UF dos Recursos Federais
    tqdm.pandas(desc="🔹 %pop  ")
    municipio['Auxilio'] = ((municipio['Beneficiarios'] /
                            municipio['pop_2022'])*100).progress_apply(lambda x: x)

    print(municipio)

    # quit()

    return municipio

##
# Processamento das UFs
##


def uf():
    print("📌 Processando UFs")

    # Cálculos
    tqdm.pandas(desc="🔹 Total ")
    uf = df.groupby(['UF'])['Valor'].sum().progress_apply(lambda x: x)
    uf = pd.DataFrame(uf)

    br_recursos = uf.sum()

    tqdm.pandas(desc="🔹 count ")
    uf['count'] = df.groupby(
        ['UF'])['Valor'].count().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 mean  ")
    uf['mean'] = df.groupby(
        ['UF'])['Valor'].mean().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 std   ")
    uf['std'] = df.groupby(
        ['UF'])['Valor'].std().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 min   ")
    uf['min'] = df.groupby(
        ['UF'])['Valor'].min().progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹  1%   ")
    uf['1%'] = df.groupby(['UF'])['Valor'].quantile(
        q=0.01).progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 50%   ")
    uf['50%'] = df.groupby(['UF'])['Valor'].quantile(
        q=0.50).progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 99%   ")
    uf['99%'] = df.groupby(['UF'])['Valor'].quantile(
        q=0.99).progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 max   ")
    uf['max'] = df.groupby(
        ['UF'])['Valor'].max().progress_apply(lambda x: x)

    # A equação essencial da PONTUAÇÃO Z (zscore) para um exemplo é:
    # z = (x – μ)/σ
    # x = metrica = Valor médio pago ao total de  Benefiário na UF
    # média (μ) = Valor médio pado ao total Beneficiários do Brasil
    # desvio padrão (σ) = Desvio padrão

    tqdm.pandas(desc="🔹 mean  ")
    br_mean = df['Valor'].mean()

    print("🔹 std   ")
    br_std = df['Valor'].std()

    tqdm.pandas(desc="🔹 zscore ")
    uf['zscore'] = ((uf['mean'] - br_mean) /
                    br_std).progress_apply(lambda x: x)

    tqdm.pandas(desc="🔹 Mun   ")
    uf['Municípios'] = df.groupby(
        ['UF'])['Municipio'].unique().progress_apply(lambda x: len(x))

    # Cálcula Percentual utilizado pela UF dos Recursos Federais
    tqdm.pandas(desc="🔹 br    ")
    uf['Perc_recursos_BR'] = uf['Valor'].progress_apply(
        lambda x: (x/br_recursos)*100).progress_apply(lambda x: x)

    # Cálculos da população das UFs
    tqdm.pandas(desc="🔹 pop_22")
    uf['pop_2022'] = municipio.groupby(
        ['UF'])['pop_2022'].sum().progress_apply(lambda x: x)

    # Cálcula Percentual utilizado pela UF dos Recursos Federais
    tqdm.pandas(desc="🔹 %pop  ")
    uf['auxilio'] = ((uf['count'] / uf['pop_2022']) *
                     100).progress_apply(lambda x: x)

    # Cálcula Percentual utilizado pela UF dos Recursos Federais
    tqdm.pandas(desc="🔹 %br  ")
    br_pop = df_ibge['pop_2022'].sum()
    uf['%br'] = ((uf['pop_2022'] / br_pop) *
                 100).progress_apply(lambda x: x)

    # Ajustes na estatistica descritiva dos recursos da UF
    uf['count'] = uf['count'].astype(int)
    uf['min'] = uf['min'].astype(int)
    uf['1%'] = uf['1%'].astype(int)
    # uf['25%'] = uf['25%'].astype(int)
    uf['50%'] = uf['50%'].astype(int)
    # uf['75%'] = uf['75%'].astype(int)
    uf['99%'] = uf['99%'].astype(int)
    uf['max'] = uf['max'].astype(int)
    uf.columns = ['Recursos', 'Beneficiarios', 'Media', 'Desvio',
                  'Minimo', 'Perc_1', 'Mediana', 'Perc_99', 'Maximo', 'zscore', 'Municipios', 'Perc_recursos_BR', 'pop_2022', 'Auxilio', 'BR']

    uf.reset_index(inplace=True)

    tqdm.pandas(desc="🔹 PerMun")
    uf['Per_municipio'] = (uf['Recursos'] / uf['Municipios']
                           ).progress_apply(lambda x: int(x))

    tqdm.pandas(desc="🔹 Percap")
    uf['Per_beneficiario'] = (
        uf['Recursos'] / uf['Beneficiarios']).progress_apply(lambda x: x)

    uf['Flag'] = uf['UF'].progress_apply(
        lambda x: f"https://raw.githubusercontent.com/bgeneto/bandeiras-br/master/imagens/{x}.png")

    # https://raw.githubusercontent.com/bgeneto/bandeiras-br/master/imagens/{x}.png
    # https://github.com/bgeneto/bandeiras-br/blob/master/imagens/{x}.png

    return uf

##
# Processamento Nacional
##


def br():
    print("📌 Processando Brasil")

    # br = uf['Brasil']

    print("🔹 Total ")
    br_total = uf['Recursos'].sum()

    # br_count = uf['Beneficiários'].sum()

    print("🔹 count ")
    br_count = df['Valor'].count()

    tqdm.pandas(desc="🔹 mean  ")
    br_mean = df['Valor'].mean()

    print("🔹 std   ")
    br_std = df['Valor'].std()

    print("🔹 min   ")
    br_min = df['Valor'].min()

    print("🔹  1%   ")
    br_1 = df['Valor'].quantile(q=0.01)

    print("🔹 Rec_1%  ")
    br_rec_1 = df[df['Valor'] < br_1]['Valor'].sum()

    print("🔹 50%   ")
    br_50 = df['Valor'].quantile(q=0.50)

    print("🔹 99%   ")
    br_99 = df['Valor'].quantile(q=0.99)

    print("🔹 Rec_1%  ")
    br_rec_99 = df[df['Valor'] > br_99]['Valor'].sum()

    print("🔹 max   ")
    br_max = df['Valor'].max()

    print("🔹 Mun   ")
    br_Mun = len(df['Municipio'].unique())

    # Cálculos da população das UFs
    print("🔹 %spop_22 ")
    br_pop = df_ibge['pop_2022'].sum()

    # Cálcula Percentual utilizado pela UF dos Recursos Federais
    print("🔹 %social ")
    br_auxilio = (br_count / br_pop) * 100

    # Cálcula Percentual utilizado pela UF dos Recursos Federais
  #  tqdm.pandas(desc="🔹 %br  ")
  #  br_br = ((br['count'] / br_pop) *
  #           100).progress_apply(lambda x: x)

    print("🔹 br_Per_municipio")
    br_Per_municipio = int(br_total / br_Mun)

    print("🔹 br_Per_beneficiario")
    br_Per_beneficiario = float(br_total / br_count)

    data = [{'br': 'Brasil', 'Recursos': br_total, 'Beneficiarios': br_count, 'Media':
            br_mean, 'Desvio': br_std, 'Minimo': br_min, 'perc_1': br_1, 'rec_1': br_rec_1, 'Mediana': br_50, 'perc_99': br_99, 'rec_99': br_rec_99, 'Maximo': br_max, 'Municipios': br_Mun, 'Per_municipio': br_Per_municipio, 'Per_beneficiario': br_Per_beneficiario, 'pop_2022': br_pop, 'auxilio': br_auxilio}]

    br = pd.DataFrame(data)

    return br


##
# Processamento das UFs
##


def gravar_resultado():
    print("📌 Processando Brasil")

    uf_output = 'dataset/nbf_202306_uf.csv'
    print(f"🔹 Gravando  {uf_output}")
    uf.to_csv(uf_output, index=True, sep=';')

    municipio_output = 'dataset/nbf_202306_mun.csv'
    print(f"🔹 Gravando  {municipio_output}")
    municipio.to_csv(municipio_output, index=True, sep=';')

    br_output = 'dataset/nbf_202306_br.csv'
    print(f"🔹 Gravando  {br_output}")
    br.to_csv(br_output, index=False, sep=';')

##
# Processamento das UFs
##


def mostra_resultado():
    print('\n', municipio, '\n')
    print('\n', uf, '\n')
    print('\n', br)
    # print('\n\n')


##
# Main
##
municipio = municipio()
print('\n')
uf = uf()
print('\n')
br = br()
print('\n')
mostra_resultado()
print('\n')
gravar_resultado()
print('\n')

df = None  # excluir

quit()


# municipio['mean'] = municipio['mean'].round(2)
# municipio['std'] = municipio['std'].round(2)

# uf = pd.DataFrame(uf)
# uf.reset_index(inplace=True)

#   uf['Brasil'] = uf['Brasil'].round(2)
#    {: .2f}

# print(df.columns.values)
# print(df.dtypes)
# df.info()

# print(df.query('NIS=nan'))
# usando consulta (avaliação e consulta funcionam apenas com colunas)
# print(df.query('Valor > 2640 & Nome.str.startswith("MARIA").values'))
# print(df.query('Valor > 0 & (NIS.str.startswith("nan").values | NIS.str.startswith("nan").values)'))
# print(df.query('Valor > 1320'))

# print(len(df))
# print(df.size)
# df.to_csv('output.csv', index=False, sep=';')
# quit()

# Listar as colunas
# df.columns.values
# print(df.dtypes)

# tqdm.pandas(desc="Convertendo para 'int'")
# print("Cálculos")
# df['SM2'] = df['Valor'].astype(int).parallel_apply(
#    lambda x: 0 if x <= SM2 else x-SM2)

# lambda x: 0 if x <= SM1 else x-SM1)

# https: // nalepae.github.io/pandarallel/user_guide/
# from pandarallel import pandarallel
# pandarallel.initialize(nb_workers=1, progress_bar=True)
# 1 = python3 nbf_data_sanitize.py  32.57s user 3.20s system 101% cpu 35.216 total
# 2 = python3 nbf_data_sanitize.py  39.67s user 3.45s system 123% cpu 35.055 total
# 3 = python3 nbf_data_sanitize.py  41.05s user 3.58s system 141% cpu 31.499 total
# 4 = python3 nbf_data_sanitize.py  46.78s user 5.45s system 149% cpu 34.929 total
# 5 = python3 nbf_data_sanitize.py  47.01s user 4.80s system 148% cpu 34.987 total
# 6 = python3 nbf_data_sanitize.py  42.24s user 4.74s system 152% cpu 30.717 total
# 7 = python3 nbf_data_sanitize.py  45.81s user 5.46s system 153% cpu 33.382 total

# tqdm.pandas(desc="🔹 Estatísticas")
# uf_estatisticas = df.groupby(
#    ['UF'])['Valor'].describe().progress_apply(lambda x: x)

# Merge
# uf = pd.merge(uf_recursos, uf_estatisticas,
#              right_index=True,
#              left_index=True)
