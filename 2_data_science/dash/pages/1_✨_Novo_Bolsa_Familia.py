#
# Estatística Descritiva
# https://medium.com/pyladiesbh/estat%C3%ADstica-descritiva-1-ed523dffb99f
# https://analisemacro.com.br/econometria-e-machine-learning/como-gerar-sumarios-de-estatisticas-descritivas/
#

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


# @st.cache_data  # Cache the dataframe so it's only loaded once
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


# @st.cache_data  # Cache the dataframe so it's only loaded once
def load_uf():
    dataset = "source/dataset/nbf_202306_uf.csv"
    uf = pd.read_csv(dataset,
                     # index_col=0,
                     # index_col='nome_da_coluna'
                     delimiter=';',
                     encoding='latin-1',
                     )
    # df_data("Date") = pd.to_datetime(df_data["Date"]) # Converte para data

    return uf


def view_uf():
    uf_colunas = ['Flag', 'UF', 'Municipios', 'Per_municipio', 'Beneficiarios', 'Per_beneficiario',
                  'pop_2022', 'Auxilio',  'Recursos',  'Perc_recursos_BR', 'Media', 'Desvio', 'Mediana', 'zscore']

    # uf.reset_index(inplace=True)

    # uf[uf_colunas].style.highlight_max(axis=0)
    st.dataframe(uf[uf_colunas],
                 column_config={
        "Flag": st.column_config.ImageColumn(
            help="Bandeira da Unidade Federativa"),

        # "UF": st.column_config.NumberColumn(
        #    help="Unidade Federativa"),

        "Municipios": st.column_config.NumberColumn(
            "Municípios",
            help="Quantidade de Municípios"),

        "Per_municipio": st.column_config.NumberColumn(
            "Rec/Município",
            # format="%,.2f",
            help="Recurso Médio aplicado por Município"),

        "Per_beneficiario": st.column_config.NumberColumn(
            "Rec/Benef",
            format="%.2f",
            help="Recurso Médio por Beneficiarios"),

        "pop_2022": st.column_config.NumberColumn(
            "Censo 2022",
            help="População no último Censo"),

        "Beneficiarios": st.column_config.NumberColumn(
            "Beneficiários",
            help="Quantidade de Beneficiarios"),

        "Media": st.column_config.NumberColumn(
            format="%.2f",
            help="Média simples dos auxilios pago aos Beneciários"),

        "Desvio": st.column_config.NumberColumn(
            format="%.2f",
            help="Desvio Padrão da Média dos auxilios pago aos Beneciários"),

        "Auxilio": st.column_config.ProgressColumn(
            "% População Auxiliada", format="%.2f",
            min_value=0, max_value=100,
            help="Percentagem de população auxiliada"),

        "Recursos": st.column_config.NumberColumn(
            "Recursos Aplicados",
            help="Total de Recursos aplicados"),

        "Perc_recursos_BR": st.column_config.ProgressColumn(
            "% Recursos Federais", format="%.2f",
            min_value=0,  max_value=100,
            help="Percentagem dos Recursos Federais aplicados"),

        "zscore": st.column_config.NumberColumn(
            "Z Score",
            format="%.3f",
            help="Quantidade de Desvios Patrão de distância da Média"),

        # "pop_2022": st.column_config.ProgressColumn(
        #    "pop_2022", format="%i",
        #    min_value=0,  max_value=int(br['pop_2022'])),

    },
        hide_index=True,
        height=990,
        # use_container_width=True
    )


# @st.cache_data  # Cache the dataframe so it's only loaded once
def load_municipio():
    dataset = "source/dataset/nbf_202306_mun.csv"
    municipio = pd.read_csv(dataset, index_col=0,
                            # index_col='nome_da_coluna'
                            delimiter=';',
                            encoding='latin-1',
                            )
    # st.write(municipio)
    return municipio


data_load_state = st.sidebar.text('Loading Dataframes: br ...')
br = load_br()
data_load_state.text('br, uf ...')
uf = load_uf()
data_load_state.text('br, uf, municipios ...')
municipio = load_municipio()
data_load_state.text('br, uf, municipios ... ok!')

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


##
# PAGE
##

st.header(
    f":rainbow[República Federativa do BRASIL =  R$ {float(br['Recursos']):,.0f}]",
    divider="orange")

if st.sidebar.toggle('Brasil Analytics'):
    # col1, col2, col3, col4, col5, col6 = st.columns(6, gap='small')
    col1, col2, col3, col4, col5 = st.columns(5, gap='small')

    with col1:
        st.info("Municípios", icon="📌")
        st.metric(label="Quantidade de Municípios",
                  value=f"{int(br['Municipios']):,.0f}")

    with col2:
        st.info("Beneficiários", icon="🎯")
        st.metric(label="Quantidade de Beneficiários",
                  value=f"{int(br['Beneficiarios']):,.0f}")

    with col3:
        st.info("1º Percentio", icon="💲")
        st.metric(label="Os 1% que recebem MENOS",
                  value=f"{float(br['rec_1']):,.0f}")
    with col4:
        st.info("do 2º ao 98º Percentio", icon="💲")
    #    uf_recursos = float(uf_filtered['Recursos'])
        st.metric(label="Total aplicado (R$)",
                  value=f"{float(br['Recursos']-br['rec_1']-br['rec_99']):,.0f}")

    with col5:
        st.info("99º Percentio", icon="💲")
        st.metric(label="Os 1% que recebem MAIS",
                  value=f"{float(br['rec_99']):,.0f}")
        # value=faixa)

    col1, col2, col3, col4, col5 = st.columns(5, gap='small')

    with col1:
        st.info("Por Município", icon="⚖️")
        permunicipio = float(br['Recursos'] / br['Municipios'])
        st.metric(label="Média por Município (R$)",
                  value=f"{permunicipio:,.0f}")
        # , help=f"""Média por Município""")

    with col2:
        st.info("Por Beneficiárioa", icon="⚖️")
        percapita = float(br['Recursos'] / br['Beneficiarios'])
        st.metric(label="Média por Beneficiário (R$)",
                  value=f"{percapita:,.2f}")
        # , help=f"""Média por Beneficiário""")

    with col3:
        st.info("Primeiro Percentio", icon="🎯")
        faixa = f"{float(br['Minimo']):,.0f} - {float(br['perc_1']):,.0f}"
        st.metric(label="Os 1% que recebem MENOS",
                  value=faixa)

    with col4:
        st.info("Mediana", icon="⚖️")
        st.metric(label="50% recebem baixo e 50% acima",
                  value=f"{float(br['Mediana']):,.0f}")

    with col5:
        st.info("Último Percentio", icon="🎯")
        faixa = f"{float(br['perc_99']):,.0f} - {float(br['Maximo']):,.0f}"
        st.metric(label="Os 1% que recebem MAIS",
                  value=faixa)

col1, col2, col3 = st.columns([2.4, 1.2, 2], gap='small')

with col1:
    # with st.container():
    # https: // zebrabi.com/guide/how-to-customize-bar-chart-in -python-plotly/
    fig_bar = px.bar(
        uf, x="UF",  y="Recursos",
        # labels={'x': 'total_bill', 'y': 'count'},
        title="<i>Distribuição dos Recursos às Unidades Federativas</i>",
        orientation="v",
        color_discrete_sequence=["#0083b8"]*len(municipio_filtered),
        template="plotly_white",
    )
    fig_bar.update_layout(
        plot_bgcolor="rgb(0,0,0,0)",
        xaxis=(dict(showgrid=False)),
        title_font=dict(size=18),
        xaxis_title="Unidades Federativas do Brasil",
        yaxis_title="Recursos Aplicados",
    )
    fig_bar.update_traces(
        # marker_color='blue',
        # marker_line_color='darkblue',
        # marker_line_width=1.5,
        opacity=0.6)
    st.plotly_chart(fig_bar, use_container_with=True)

with col2:
    # resultado = [numero for numero in range(20) if numero % 2 == 0]
    # resultado = ['1' if numero % 5 == 0 else '0' for numero in range(16)]

    # https: // plotly.com/python/pie-charts/
    labels = uf['UF']
    values = uf['Recursos']
    pull = [0.2 if destaque == uf_selecionada else 0 for destaque in uf['UF']]
    # pull is given as a fraction of the pie radius
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=.4,
                pull=pull)
        ]
    )
    st.plotly_chart(fig, use_container_with=True)

# Dica: Converter Index para Column
# https://datatofish.com/index-to-column-pandas-dataframe/
# df_brasil = pd.DataFrame(df_brasil)
# df_brasil.reset_index(inplace=True)

# st.sidebar.write(df_brasil.dtypes)

# Cálcula Percentual utilizado pela UF dos Recursos Federais
# df_brasil['perc'] = df_brasil['Total'].apply(lambda x: (x/Recursos_Brasil*100))


# st.sidebar.markdown(f"""<br>""", unsafe_allow_html=True)

if st.sidebar.toggle('UF Analytics'):
    st.header(
        f":rainbow[{uf_selecionada} = R$ {float(uf_filtered['Recursos']):,.0f}]", divider="orange")

    # col1, col2, col3, col4, col5, col6 = st.columns(6, gap='small')
    col1, col2, col3, col4, col5, col6 = st.columns(6, gap='small')

    with col1:
        st.info("Municípios", icon="📌")
        uf_municipios = int(uf_filtered['Municipios'])
        st.metric(label="Quantidade de Municípios",
                  value=f"{uf_municipios:,.0f}")

    with col2:
        st.info("Beneficiarios", icon="🎯")
        uf_auxilio = float(uf_filtered['Auxilio'])
        uf_beneficiados = int(uf_filtered['Beneficiarios'])
        st.metric(label=f"{uf_auxilio:,.2f}% da população do Censo 2022",
                  value=f"{uf_beneficiados:,}")

    col1, col2, col3, col4, col5, col6 = st.columns(6, gap='small')

    with col1:
        st.info("Por Município", icon="⚖️")
        per_municipio = int(uf_filtered['Per_municipio'])
        delta = per_municipio - int(br['Per_municipio'])
        st.metric(label="Média por Município (R$)",
                  value=f"{per_municipio:,.0f}",
                  delta=f"{delta:,.0f}",
                  )
        # , help=f"""Média por Município""")

    with col2:
        st.info("Por Beneficiárioa", icon="⚖️")
        percapita = float(uf_filtered['Recursos'] /
                          uf_filtered['Beneficiarios'])
        per_beneficiario = float(uf_filtered['Per_beneficiario'])
        delta = per_beneficiario - float(br['Per_beneficiario'])
        st.metric(label="Média por Beneficiário (R$)",
                  value=f"{per_beneficiario:,.2f}",
                  delta=f"{delta:,.0f}",
                  )
        # , help=f"""Média por Beneficiário""")

    with col3:
        st.info("Primeiro Percentio", icon="🎯")
        faixa = f"{float(uf_filtered['Minimo']):,.0f} - {float(uf_filtered['Perc_1']):,.0f}"
        st.metric(label="Os 1% que recebem MENOS",
                  value=faixa)

    with col4:
        st.info("Mediana", icon="⚖️")
        st.metric(label="50% recebem baixo e 50% acima",
                  value=f"{float(uf_filtered['Mediana']):,.0f}")

    with col5:
        st.info("Último Percentio", icon="🎯")
        faixa = f"{float(uf_filtered['Perc_99']):,.0f} - {float(uf_filtered['Maximo']):,.0f}"
        st.metric(label="Os 1% que recebem MAIS",
                  value=faixa)

    with col6:
        st.info("Z Score", icon="⚖️")
        # faixa = f"{float(uf_filtered['Perc_99']):,.0f} - {float(uf_filtered['Maximo'])#:,.0f}"
        st.metric(label="Pontuação Z",
                  value=f"{float(uf_filtered['zscore']):,.3f}")


if st.sidebar.toggle('UF Dataframe'):
    view_uf()


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
st.sidebar.markdown(f""" <br><br> """, unsafe_allow_html=True)
# st.sidebar.divider()
st.sidebar.image(
    "https://avatars.githubusercontent.com/u/93828234?s=400&u=c8291445091f454295fa625f563c98c7bada976c&v=4")

# st.sidebar.write(":rainbow[Marcos Antônio de Carvalho]")
st.sidebar.markdown(
    f"""
    🦉:rainbow[Marcos Antônio de Carvalho]
    :blue[:copyright:] :orange[2023] :green[by] [owl-arch](https://github.com/owl-arch)""", unsafe_allow_html=True)


st.sidebar.divider()
with st.container():
    if st.sidebar.toggle('Debug UF'):
        # st.write(uf.dtypes)

        st.write(uf)
        # uf.set_index("UF")
        # view_uf()
        # st.dataframe(data=uf, use_container_width=True)

    if st.sidebar.toggle('Debug: Municipios'):
        # if st.sidebar.checkbox('Municipios'):
        st.dataframe(data=municipio_filtered, use_container_width=True)
        st.write("Shape", municipio_filtered.shape)

    # if st.sidebar.checkbox('Brasil'):
    if st.sidebar.toggle('Debug: Brasil'):
        # st.dataframe(data=uf, use_container_width=True)
        st.write(br)
        # st.write("Shape", uf.shape)
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
