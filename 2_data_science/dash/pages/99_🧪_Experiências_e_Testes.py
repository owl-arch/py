import pandas as pd
import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Page A", page_icon="🦉", layout="wide")

Logo = {"image": 'image/koruja_70.png',
        "height": 60}
add_logo(Logo["image"], height=Logo["height"])
st.session_state["Logo"] = Logo

st.sidebar.markdown(
    f"""
    <div style="text-align: justify;">
    <img src="https://avatars.githubusercontent.com/u/93828234?s=400&u=c8291445091f454295fa625f563c98c7bada976c&v=4">
    Marcos Antônio de  <strong>Carvalho</strong> 
    </div>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    f":blue[:copyright:] :orange[2023] :green[by] [owl-arch](https://github.com/owl-arch)")

##
# PAGE
##

Header = st.session_state["Header"]
st.header(Header["title"], help=Header["help"], divider=Header["divider"])

Data = st.session_state["Data"]
states = Data["UF"].unique()

tab1, tab2 = st.tabs(["UF", "Municípios"])

with tab1:
    st.write(states)
    st.write(states.shape)

with tab2:
    # st.write(data)
    st.dataframe(data=Data["UF"], use_container_width=True)


st.divider()

st.write("# Page A")
st.write("## Page A")
st.write("### Page A")
st.write("#### Page A")
st.write("- item 1")
st.write("- item 2")

st.header("Header Page A")
st.subheader("SubHeader Page A")
st.title("Title Título")


col1, col2 = st.columns(2, gap="small")

with col1:
    # with st.container():
    fig_bar = px.bar(
        df_filtered, x="Total", y="Municipio",
        title="<center>Total de Pagamentos por Município</centerb>",
        orientation="h",
        color_discrete_sequence=["#0083b8"]*len(df_filtered),
        template="plotly_white",
    )
    fig_bar.update_layout(
        plot_bgcolor="rgb(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )
    st.plotly_chart(fig_bar, use_container_with=True)

#    graf_bar = px.bar(df_filtered, x="Municipio", y="Total",
#                   title="Total de Pagamentos por Município")
#    col1.plotly_chart(graf_bar, use_container_with=True))

with col2:
    # with st.container():
    df_data = st.session_state["Data"]
    graf_pie = px.pie(df_filtered, values="Total", names="Municipio",
                      title="Percentual de Pagamentos por Município ")
    st.plotly_chart(graf_pie, use_container_with=True)
