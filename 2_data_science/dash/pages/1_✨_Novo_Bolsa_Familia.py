
##
# Libraries and Frameworks
##


import streamlit as st  # pip3 install streamlit
# from streamlit_option_menu import option_menu
from streamlit_extras.app_logo import add_logo

import pandas as pd

import numpy as np

import plotly.express as px  # pip3 install plotly
import plotly.graph_objects as go

import matplotlib as plt

import openai

from config import rodape

# from numerize.numerize import numerize

##
# Configurations
##

st.set_page_config(page_title="Analytics", page_icon="🦉", layout="wide")

Logo = {"image": 'image/owl_65.png',
        "height": 60}
add_logo(Logo["image"], height=Logo["height"])
st.session_state["Logo"] = Logo

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

##
# Data Ingestion
# Ingestão de Dados
##


@st.cache_data  # Cache the dataframe so it's only loaded once
def load_br():
    dataset = "source/dataset/nbf_202306_br.csv"
    br = pd.read_csv(dataset, index_col=0,
                     # index_col='nome_da_coluna'
                     delimiter=';',
                     encoding='latin-1',
                     )
    # df_data("Date") = pd.to_datetime(df_data["Date"]) # Converte para data
    # st.dataframe(data=uf, use_container_width=True)
    return br


#  @st.cache_data  # Cache the dataframe so it's only loaded once
def load_uf():
    dataset = "source/dataset/nbf_202306_uf.csv"
    uf = pd.read_csv(dataset,
                     # index_col=0,
                     # index_col='nome_da_coluna'
                     delimiter=';',
                     encoding='latin-1',
                     )
    # df_data("Date") = pd.to_datetime(df_data["Date"]) # Converte para data
    uf_colunas = ['Flag', 'UF', 'Municipios', 'pop_2022',  'Beneficiarios',
                  'Auxilio',  'Recursos',  'Perc_recursos_BR', 'Media', 'Desvio', 'Mediana']

    # st.write(uf["pop_2022"].max())
    # max = uf["pop_2022"].max()
    # st.write(max)

    # st.write(uf.dtypes)
    # st.write(br)
    uf.reset_index(inplace=True)
    st.dataframe(uf[uf_colunas],
                 column_config={
        "Flag": st.column_config.ImageColumn(),
        "pop_2022": st.column_config.NumberColumn("Censo 2022"),
        "Beneficiarios": st.column_config.NumberColumn("Beneficiários"),
        "Media": st.column_config.NumberColumn(format="%.2f"),
        "Desvio": st.column_config.NumberColumn(format="%.2f"),

        # "Perc_recursos_BR": st.column_config.NumberColumn(
        #    "% Recursos", format="%.2f"),


        "Auxilio": st.column_config.ProgressColumn(
            "% População Auxiliada", format="%.2f",
            min_value=0, max_value=100),

        "Recursos": st.column_config.NumberColumn("Recursos Aplicados"),
        "Perc_recursos_BR": st.column_config.ProgressColumn(
            "% Recursos Federais", format="%.2f",
            min_value=0,  max_value=100),


        # "pop_2022": st.column_config.ProgressColumn(
        #    "pop_2022", format="%i",
        #    min_value=0,  max_value=int(br['pop_2022'])),

    }
    )
    # uf["Censo 2022"].max()
    # st.dataframe(data=uf, use_container_width=True)
    return uf


@st.cache_data  # Cache the dataframe so it's only loaded once
def load_municipio():
    dataset = "source/dataset/nbf_202306_mun.csv"
    municipio = pd.read_csv(dataset, index_col=0,
                            # index_col='nome_da_coluna'
                            delimiter=';',
                            encoding='latin-1',
                            )
    # st.write(municipio)
    return municipio


br = load_br()
uf = load_uf()
municipio = load_municipio()


##
# PAGE
##

Header = st.session_state["Header"]
st.header(Header["title"], help=Header["help"], divider=Header["divider"])

uf_selecionada = st.sidebar.selectbox(
    "Selecione oa UF:", uf["UF"].sort_values().unique())

# UF  Filtrado
uf_filtered = uf[uf['UF'] == uf_selecionada]

# Municípios  Filtrados
municipio_filtered = municipio[municipio["UF"] ==
                               uf_selecionada]
municipio_filtered = municipio_filtered.sort_values(by=["UF"], ascending=False)
municipio_filtered = pd.DataFrame(municipio_filtered)
municipio_filtered.reset_index(inplace=True)

st.sidebar.divider()

with st.container():
    # st.sidebar.subheader('Mostra:')
    if st.sidebar.checkbox('Brasil'):
        # st.dataframe(data=uf, use_container_width=True)
        st.write(br)
        # st.write("Shape", uf.shape)

    if st.sidebar.checkbox('Unidades Federativas'):
        # st.dataframe(data=uf, use_container_width=True)
        st.write(uf)
        # st.write("Shape", uf.shape)

    # if st.sidebar.toggle('Municipios'):
    if st.sidebar.checkbox('Municipios'):
        st.dataframe(data=municipio_filtered, use_container_width=True)
        st.write("Shape", municipio_filtered.shape)


# df_brasil = df_data.groupby(['UF'])['Total'].sum()  # Dataframe Brasil
# Recursos_Brasil = df_brasil.sum()

# Dica: Converter Index para Column
# https://datatofish.com/index-to-column-pandas-dataframe/
# df_brasil = pd.DataFrame(df_brasil)
# df_brasil.reset_index(inplace=True)

# st.sidebar.write(df_brasil.dtypes)

# Cálcula Percentual utilizado pela UF dos Recursos Federais
# df_brasil['perc'] = df_brasil['Total'].apply(lambda x: (x/Recursos_Brasil*100))


# st.sidebar.markdown(f"""<br>""", unsafe_allow_html=True)

# col1, col2, col3, col4, col5, col6 = st.columns(6, gap='small')
col1, col2, col3, col4, col5 = st.columns(5, gap='small')

with col1:
    st.info("Unidade Federativa", icon="📌")
    uf_municipios = int(uf_filtered['Municipios'])
    st.metric(
        label=f"{uf_municipios:,.0f} Municipios", value=uf_selecionada)

with col2:
    st.info("Beneficiarios", icon="🎯")
    # st.write(uf_filtered)
    uf_auxilio = float(uf_filtered['Auxilio'])
    uf_beneficiados = int(uf_filtered['Beneficiarios'])
    st.metric(label=f"{uf_auxilio:,.2f}% da população do Censo 2022",
              value=f"{uf_beneficiados:,}")

with col3:
    st.info("Recursos Públicos", icon="💲")
    uf_recursos = float(uf_filtered['Recursos'])
    st.metric(label="Total aplicado (R$)", value=f"{uf_recursos:,.0f}")

with col4:
    st.info("Por Beneficiárioa", icon="⚖️")
    percapita = float(uf_filtered['Recursos'] / uf_filtered['Beneficiarios'])
    st.metric(label="Média por Beneficiário (R$)",
              value=f"{percapita:,.2f}")
    # , help=f"""Média por Beneficiário""")

with col5:
    st.info("Por Município", icon="⚖️")
    permunicipio = float(uf_filtered['Recursos'] / uf_filtered['Municipios'])
    st.metric(label="Média por Município (R$)",
              value=f"{permunicipio:,.0f}")
    # , help=f"""Média por Município""")

# st.markdown("""---""")

col1, col2, col3 = st.columns([2.4, 1.2, 2], gap='large')

with col1:
    # with st.container():
    fig_bar = px.histogram(
        municipio_filtered, y="Municipio",  x="Recursos",
        # title="<i>Total de Pagamentos por Município</i>",
        orientation="h",
        color_discrete_sequence=["#0083b8"]*len(municipio_filtered),
        template="plotly_white",
    )
    fig_bar.update_layout(
        plot_bgcolor="rgb(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )
    st.plotly_chart(fig_bar, use_container_with=True)

with col2:
    # https: // plotly.com/python/pie-charts/
    labels = uf['UF']
    values = uf['Recursos']
    # pull is given as a fraction of the pie radius
    fig = go.Figure(
        data=[go.Pie(
            labels=labels,
            values=values,
            hole=.4,
            pull=[0, 0, 0, 0, 0, 0, 0, 0, 0,  0.2, 0])])
    st.plotly_chart(fig, use_container_with=True)


# with st.container():
#    fig = px.treemap(df_brasil, path=['UF'], values='perc',
#                     color='UF', hover_data=['perc'],
#                     color_continuous_scale='RdBu',
#                     color_continuous_midpoint=np.average(df_brasil['Total'], #weights=df_brasil['perc']))
#    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
#    st.plotly_chart(fig, use_container_with=True)

#    # https: // plotly.com/python/pie-charts/
#    labels = df_brasil['UF']
#    values = df_brasil['Total']
#    # pull is given as a fraction of the pie radius
#    # fig = go.Figure(
#    #    data=[go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0])])
#    fig = go.Figure(
#        data=[go.Pie(labels=labels, values=values, hole=.3, pull=[0, 0, 0.2, 0])])
#    st.plotly_chart(fig, use_container_with=True)

##
# Rodapé
##

# rodape()
# st.sidebar.markdown(f""" <br><br><br> """, unsafe_allow_html=True)
# st.sidebar.divider()
st.sidebar.image(
    "https://avatars.githubusercontent.com/u/93828234?s=400&u=c8291445091f454295fa625f563c98c7bada976c&v=4")

# st.sidebar.write(":rainbow[Marcos Antônio de Carvalho]")
st.sidebar.markdown(
    f"""
    🦉:rainbow[Marcos Antônio de Carvalho]
    :blue[:copyright:] :orange[2023] :green[by] [owl-arch](https://github.com/owl-arch)""", unsafe_allow_html=True)


##
# GPT
##
# https://www.youtube.com/watch?v=6dsUQfsovCw&t=698s
# Crie dashboards incríveis usando PYTHON, STREAMLIT e CHATGPT
##

openai.api_key = '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'
# completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages[{"role": #user", "content": "Hello!"}])#

# "content": f'O dataset a seguir corresponde a metricas do auxilio social do governo #federal do Brasil, conhecido como do novo bolsa familia. Me informe 5 insights #sobre #este dataset {municipio_filtered}'}

# response = openai.ChatCompletion.create(
#    model="gpt-3.5-turbo",
#    messages=[
#        {"role": "system", "content": "You are a helpful assistant."},
#       {"role": "user", "content": "Who won the world series in 2020?"},
#       {"role": "assistant",
#            "content": "The Los Angeles Dodgers won the World Series in 2020."},
#       {"role": "user", "content": "Where was it played?"}
#    ]
# )
# set.markdown(response['choices'][0]['message']['content'])
