
##
# Rodapé
##
def rodape():
    st.sidebar.markdown(f""" <br><br><br> """, unsafe_allow_html=True)
    # st.sidebar.divider()
    st.sidebar.image(
        "https://avatars.githubusercontent.com/u/93828234?s=400&u=c8291445091f454295fa625f563c98c7bada976c&v=4")

    # st.sidebar.write(":rainbow[Marcos Antônio de Carvalho]")
    st.sidebar.markdown(
        f"""
        🦉:rainbow[Marcos Antônio de Carvalho]
        :blue[:copyright:] :orange[2023] :green[by] [owl-arch](https://github.com/owl-arch)""", unsafe_allow_html=True)
