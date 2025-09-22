import streamlit as st

# Configuración general del sitio
st.set_page_config(page_title="Música Urbana Chilena", layout="wide")

# Configuracion de logo
     st.logo(
    "logokid.jpg"   
)

# Barra lateral para navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.radio("Ir a:", [
    "Inicio",
    "Kidd Voodoo",
    "Young Cister",
    "Easykid",
    "Yan Block"
])

# Página Inicio
if pagina == "Inicio":
    st.title("Música Urbana Chilena")
    st.write("Este sitio contiene a mis cantantes favoritos.")
    st.image("4f.jpeg", caption="Música Urbana Chilena")
    st.video("https://www.youtube.com/watch?v=cMcDs-MWeWA&ab_channel=KiddVoodoo")

# Página Kidd Voodoo
elif pagina == "Kidd Voodoo":
    st.header("Kidd Voodoo")
    st.write("Kidd Voodoo es un rapero chileno originario de Santiago, conocido por su estilo Latin Trap que mezcla autotune y sintetizadores.  Empezó en la banda indie 'Resonancia Etérea' y luego inició su carrera solista en 2020 con el EP 'Pa los satiros Vol.1'.  Es parte del colectivo 'Los 4F'.  Su música combina ritmos urbanos con letras melancólicas que expresan emociones profundas.")
    st.image("kidd tutu.jpeg", caption="Kidd Voodoo")
    st.video("https://www.youtube.com/watch?v=f--e5fca2Jg&ab_channel=KiddVoodoo")

# Página Young Cister
elif pagina == "Young Cister":
    st.header("Young Cister")
    st.write("Young Cister es un artista urbano chileno, conocido por su versatilidad en reguetón, trap y ritmos latinos Miembro de 'Los 4F', ha colaborado con Kidd Voodoo y otros artistas destacadosSus letras mezclan fiesta y sentimientos, creando un sonido único en la escena urbana")
    st.image("jovencisterna.jpg", caption="Young Cister")
    st.video("https://www.youtube.com/watch?v=u6Fkx2I2ksI&ab_channel=YoungCisterVEVO")

# Página Easykid
elif pagina == "Easykid":
    st.header("Easykid")
    st.write("Easykid es un compositor y cantante chileno de música urbana, parte del grupo 'Los 4F'.  Combina trap y reguetón con un estilo melódico que ha ganado reconocimiento en Chile.   Ha colaborado con destacados artistas urbanos del país.")
    st.image("easykid.jpeg", caption="Easykid")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3")

# Página Yan Block
elif pagina == "Yan Block":
    st.header("Yan Block")
    st.write("the best yan block")
    st.image("yanblock.jpg", caption="Yan Block")
    st.video("https://www.youtube.com/watch?v=5M_n2UCe7DQ&ab_channel=YanBlock")

# Comentarios y explicaciones
# Cada página usa multimedia y texto con información actualizada y widgets interactivos.
# Cambia las URLs multimedia para ajustarlas a tu gusto o temática específica.


