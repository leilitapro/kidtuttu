# Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("World of Warcraft")
st.badge("nuevo", color="green", icon=":material/chevron_right:")

# Sutítulo
st.header("Un Vistazo al Mundo de Azeroth: World of Warcraft", divider=True)
st.image("wow_classic.jpg", caption="World of Warcraft Classic: Ragnaros")
st.write(
"""
**World of Warcraft** (WoW) es un videojuego de rol multijugador masivo en línea (MMORPG) desarrollado y distribuido por Blizzard Entertainment. Lanzado originalmente en 2004, WoW se ha convertido en uno de los títulos más influyentes y exitosos de la historia de los videojuegos, atrayendo a millones de jugadores en todo el mundo a su vasto universo de fantasía.

El juego se desarrolla en el mundo ficticio de Azeroth, un planeta lleno de magia, conflictos y criaturas míticas. Los jugadores eligen entre dos facciones principales, la Alianza y la Horda, cada una con sus propias razas y motivaciones. La Alianza está formada por razas como humanos, enanos, elfos de la noche y gnomos, mientras que la Horda incluye orcos, no-muertos, tauren y trolls.

Una vez que un jugador crea su personaje, puede explorar libremente el mundo, completando misiones, luchando contra monstruos y mazmorras, y subiendo de nivel para adquirir nuevas habilidades y equipo. El juego es conocido por su rica historia, sus personajes memorables y su constante evolución a través de expansiones que añaden nuevo contenido, zonas y desafíos.

World of Warcraft no es solo un juego, es una experiencia social. Los jugadores pueden formar grupos con otros para enfrentar desafíos más grandes, unirse a gremios para colaborar y competir, y participar en batallas épicas jugador contra jugador (PvP). Desde sus épicos raids contra poderosos jefes hasta sus emocionantes arenas de combate, WoW ofrece una variedad de actividades que mantienen a los jugadores inmersos durante miles de horas.

En resumen, World of Warcraft es un titán del género MMORPG que ha definido una era. Es un mundo persistente y vibrante, lleno de aventuras, camaradería y una historia en constante expansión que sigue cautivando a jugadores de todas las edades.
"""
    )