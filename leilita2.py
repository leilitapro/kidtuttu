import streamlit as st

st.set_page_config(
    page_title="Este es mi sitio",
    page_icon=":sunglasses:"
    )

st.title("miau")
st.badge("jovencister", color="green", icon=":material/done_outline:")
st.write("Este es un sitio web sobre el joven cister")

st.divider()

st.header("qloo*", divider=True)
col1, col2 = st.columns(2)
col1.video("https://youtu.be/u6Fkx2I2ksI")
col2.write(" joven cister")
col1.write("el mejor tema")
col1.write("Texto en **LOS4F**")

col2.image("jovencisterna.jpg", caption=" temazo del jovencisterna")