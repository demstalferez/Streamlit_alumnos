#PRIMERO IMPORTAMOS LAS LIBRERIAS A USAR
import streamlit as st
import pandas as pd
import plotly.express as px

#---------------------------------------------------------------------------

#SETUP DE LA APP 
# De layout podemos usar wide or centered
st.set_page_config(page_title="Mi primera app", page_icon=":tada:", layout="centered")

#---------------------------------------------------------------------------


#TEXTOS
st.title("Mi primera app") # Titulo principal

#Encabezados 
st.header("Encabezado 1") # Encabezado 1
st.subheader("Encabezado 2") # Encabezado 2

#texto normal 
st.text("Hola mundo") # Texto normal

#markdown
st.markdown("Hola **mundo**") # Texto en markdown

#latex
st.latex(r"""a^2 + b^2 = c^2""") # Texto en latex

#code 
st.code("print('Hola mundo')", language="python") # Texto en code

#Informacion, advertencias y errores
st.info("Esto es una info") # Info
st.success("Esto es un success") # Success
st.warning("Esto es un warning") # Warning
st.error("Esto es un error") # Error
st.exception("Esto es una exception") # Exception

#---------------------------------------------------------------------------

# Medios y recursos
# Imagenes (la ruta puede ser local o una url)
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", caption="Streamlit", width=200)

#audios
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3") # Audio

#videos
st.video("https://www.youtube.com/watch?v=2Vv-BfVoq4g") # Video


#---------------------------------------------------------------------------

df = pd.DataFrame({
    "col1": [1, 2, 3, 4],
    "col2": [5, 6, 7, 8],
    "col3": [9, 10, 11, 12]
})

st.dataframe(df) # Dataframe

#---------------------------------------------------------------------------

