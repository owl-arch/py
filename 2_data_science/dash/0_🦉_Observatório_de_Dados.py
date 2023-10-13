import streamlit as st  # pip3 install streamlit
from streamlit_extras.app_logo import add_logo

import pandas as pd

import plotly.express as px  # pip3 install plotly
import matplotlib as plt


st.set_page_config(page_title="Koruja", page_icon="🦉", layout="wide")

Logo = {"image": 'image/owl_65.png',
        "height": 60}
add_logo(Logo["image"], height=Logo["height"])
st.session_state["Logo"] = Logo

Header = {"title": ':rainbow[Novo Bolsa Familia]',
          "help": 'Novo programa de auxilio social do Governo Federal',
          "divider": "orange"}
# st.header(Header["title"], help=Header["help"], divider=Header["divider"])
st.session_state["Header"] = Header


# if "Data" not in st.session_state:
#    data_load_state = st.text('Loading data...')
#    df_data = load_datafile()
#    st.session_state["Data"] = df_data
#   data_load_state.text('Loading data...done!')


##
# HOME
##

st.header(":owl: :rainbow[Data Observatory]")
st.markdown(
    """
    <div style="text-align: justify;">
    Texto de Introdução
    <strong>.....</strong> 
    </div>
    """,
    unsafe_allow_html=True
)

##
# Rodapé
##

# rodape()
st.sidebar.markdown(f""" <br><br><br> """, unsafe_allow_html=True)
# st.sidebar.divider()
st.sidebar.image(
    "https://avatars.githubusercontent.com/u/93828234?s=400&u=c8291445091f454295fa625f563c98c7bada976c&v=4")

# st.sidebar.write(":rainbow[Marcos Antônio de Carvalho]")
st.sidebar.markdown(
    f"""
    🦉:rainbow[Marcos Antônio de Carvalho]
    :blue[:copyright:] :orange[2023] :green[by] [owl-arch](https://github.com/owl-arch)""", unsafe_allow_html=True)
