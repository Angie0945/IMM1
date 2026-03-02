import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('liebbre-tortuga-cr.jpg')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Escribe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula.")
st.write(
    Había una vez una liebre muy vanidosa que se pasaba todo el día presumiendo de lo rápido que podía correr.  
Cansada de siempre escuchar sus alardes, la tortuga la retó a competir en una carrera,
Que chistosa que eres tortuga, debes estar bromeando—dijo la liebre mientras se reía a carcajadas,
Ya veremos liebre, guarda tus palabras hasta después de la carrera— respondió la tortuga,
Al día siguiente, los animales de el bosque se reunieron para presenciar la carrera. 
Todos querían ver si la tortuga en realidad podía vencer a la liebre,
El oso comenzó la carrera gritando: —¡En sus marcas, listos, ya! La liebre se adelantó inmediatamente, corrió y corrió más rápido que nunca. 
Luego, miró hacia atrás y vio que la tortuga se encontraba a unos pocos pasos de la línea de inicio,
Tortuga lenta e ingenua—pensó la liebre—. 
¿ Por qué habrá querido competir, si no tiene ninguna oportunidad de ganar? Confiada en que iba a ganar la carrera, la liebre decidió parar en medio de el camino para descansar debajo de un árbol. 
La fresca y agradable sombra de el árbol era muy relajante, tanto así que la liebre se quedó dormida,
Mientras tanto, la tortuga siguió caminando lento, pero sin pausa,
Estaba decidida a no darse por vencida,
Pronto, se encontró con la liebre durmiendo plácidamente,
¡La tortuga estaba ganando la carrera! Cuando la tortuga se acercó a la meta, todos los animales de el bosque comenzaron a gritar de emoción,
Los gritos despertaron a la liebre, que no podía dar crédito a sus ojos: la tortuga estaba cruzando la meta y ella había perdido la carrera. 
        )
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
