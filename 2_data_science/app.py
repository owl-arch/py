##
# Streamlit - Como Criar Sites com Python - Aplicação Web para Dados
# https://www.youtube.com/watch?v=0sxWFeFlsHs
#
# É o fim do Power BI? Criando Dashboard com Python em 15 minutos
# https://www.youtube.com/watch?v=P6E_Kts9pxE&t=214s
##


import streamlit as st  # pip3 install streamlit
import pandas as pd
import plotly.express as px  # pip3 install plotly

import matplotlib as plt
from tqdm import tqdm


@st.cache_data
def carregar_dados():
    file_input = '/root/datasets/Brasil_202306_NovoBolsaFamilia.csv'
    colunas_selecionadas_bolsa_familia = ['Municipio',
                                          'UF',
                                          'Total',
                                          'count',
                                          'mean',
                                          'std',
                                          'min',
                                          '25%',
                                          '50%',
                                          '75%',
                                          'max']
    # encoding 'latin-1' é o mesmo que 'ISO-8859-1'
    tabela = pd.read_csv(file_input,
                         delimiter=';',
                         encoding='ISO-8859-1',
                         nrows=50,
                         usecols=colunas_selecionadas_bolsa_familia
                         )
    return tabela


st.set_page_config(page_title="My App Streamlit", layout="wide")
# st.set_page_config(page_title="My App Streamlit")

teste = st.sidebar.selectbox("teste?", ["7d", "14d", "30d", "90d"])

with st.container():
    st.subheader("Meu primeiro site com o Streamlit")
    st.title("Dashboard de Contratos")
    st.write("Informações sobre contratos fechados em 2023")
    st.write("Visite [Meu Github](https://github.com/owl-arch)")


with st.container():
    st.write("---")
    col1, col2 = st.columns(2)
    col3 = st.columns(1)
    col4, col5 = st.columns(2)
    df = carregar_dados()
    dias = st.sidebar.selectbox("Quantos dias?", ["7d", "14d", "30d", "90d"])
    ndias = int(dias.replace("d", ""))
    # df = df[-ndias]

    graf = px.bar(df, x="Municipio", y="Total",
                  title="Total de Pagamentos por Município")
    col1.plotly_chart(graf)

    # graf_1 = px.bar(df, x="Municipio", y="Total",
    #                title="teste", orientation="h")
    # ol5.plotly_chart(graf_1)

    graf_2 = px.pie(df, values="Total", names="Percentual de Pagamentos",
                    title="teste")
    col2.plotly_chart(graf_2)

    col4.write(df)

with st.container():
    st.write("---")
    text = st.text_input('Qual seu nome')
    image = st.file_uploader(
        '../../event-driven-stack/image/eda', type=['png'])
