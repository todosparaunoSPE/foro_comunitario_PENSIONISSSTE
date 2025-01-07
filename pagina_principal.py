# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:52:26 2025

@author: jperezr
"""

import streamlit as st

# Título y descripción de la aplicación
st.set_page_config(page_title="Foro Comunitario de AFORE PENSIONISSSTE", page_icon="💬", layout="wide")
st.title("💬 Foro Comunitario de AFORE PENSIONISSSTE")
st.markdown("""
¡Bienvenidos al foro de AFORE PENSIONISSSTE! Este es un espacio creado para que puedas compartir tus experiencias, resolver dudas y aprender más sobre el sistema de pensiones y el sorteo anual de AFORE PENSIONISSSTE.
""")

# Sección de ayuda
st.sidebar.title("Ayuda")
st.sidebar.markdown("""
### Cuéntanos un poco sobre tu experiencia con el sistema de pensiones:
En esta sección, queremos conocer tu experiencia con el sistema de pensiones AFORE PENSIONISSSTE. Comparte tu opinión sobre cómo ha sido tu experiencia gestionando tu ahorro para el retiro, si tienes dudas sobre el proceso o si deseas compartir algún consejo que pueda ayudar a otros usuarios.

### Queremos conocer tu opinión sobre el Sorteo AFORE PENSIONISSSTE 2025:
Cada año, AFORE PENSIONISSSTE organiza un sorteo para incentivar el ahorro para el retiro de los trabajadores. Nos gustaría saber qué piensas sobre este sorteo. ¿Lo conoces? ¿Cómo te enteraste? ¿Qué premios te gustaría que se ofrecieran? ¿Crees que este sorteo beneficia a los trabajadores?

¡Te invitamos a dejar tus comentarios y preguntas en el foro!

### Desarrollado por: 
- Javier Horacio Pérez Ricárdez    
""")

# Preguntas principales en el foro
st.subheader("👉 Cuéntanos un poco sobre tu experiencia con el sistema de pensiones")
st.markdown("""
- ¿Cómo ha sido tu experiencia con el sistema de pensiones AFORE PENSIONISSSTE?
- ¿Tienes alguna duda o sugerencia sobre el sistema de pensiones?
- ¿Qué consejo le darías a las personas que están empezando a ahorrar para su retiro?
""")

st.subheader("👉 Queremos conocer tu opinión sobre el Sorteo AFORE PENSIONISSSTE 2025")
st.markdown("""
- ¿Conoces el sorteo de AFORE PENSIONISSSTE que se realiza cada año?
- ¿Cómo te enteraste del sorteo de AFORE PENSIONISSSTE?
- ¿Qué premios te gustaría que se ofrecieran en el sorteo de AFORE PENSIONISSSTE?
- ¿Consideras que el sorteo beneficia a los trabajadores que tienen su dinero en PENSIONISSSTE?
- ¿Qué sugerencias tienes para mejorar el sorteo de AFORE PENSIONISSSTE?
""")

# Estilo adicional con CSS
st.markdown("""
<style>
    .stButton > button {
        background-color: #0072B1;
        color: white;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #005f8c;
    }
</style>
""", unsafe_allow_html=True)