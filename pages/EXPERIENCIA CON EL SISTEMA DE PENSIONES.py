# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 15:00:37 2025

@author: jperezr
"""

import streamlit as st
import json
import os

st.set_page_config(page_title="Foro Comunitario de Pensionissste", page_icon="💬", layout="wide")

# Estilo de fondo
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background:
radial-gradient(black 15%, transparent 16%) 0 0,
radial-gradient(black 15%, transparent 16%) 8px 8px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
background-color:#282828;
background-size:16px 16px;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Archivo donde se guardarán los comentarios
comments_file = 'experiencias.json'

# Función para cargar comentarios desde el archivo
def load_comments():
    if os.path.exists(comments_file):
        with open(comments_file, 'r') as f:
            return json.load(f)
    return []

# Función para guardar comentarios en el archivo
def save_comments(comments):
    with open(comments_file, 'w') as f:
        json.dump(comments, f)

# Título de la aplicación

st.title("💬 Foro Comunitario de Pensionissste")
st.markdown("¡Bienvenidos al foro de PENSIONISSSTE! Este es un espacio creado para que puedas compartir tus experiencias, resolver dudas y aprender más sobre cómo aprovechar al máximo tu ahorro para el retiro.")

# Cargar comentarios existentes
if 'comments' not in st.session_state:
    st.session_state.comments = load_comments()

# Función para agregar un nuevo comentario
def add_comment():
    comment = st.session_state.new_comment
    if comment:
        st.session_state.comments.append(comment)
        save_comments(st.session_state.comments)  # Guardar en el archivo
        st.session_state.new_comment = ""

# Formulario para agregar comentarios
st.subheader("👉 Cuéntanos un poco sobre tu experiencia con el sistema de pensiones:")
comment_input = st.text_input("Comentario:", key='new_comment', on_change=add_comment)

# Diseño de columnas para mostrar comentarios
st.subheader("Comentarios:")
if st.session_state.comments:
    cols = st.columns(3)  # Crear tres columnas
    for i, comment in enumerate(st.session_state.comments):
        cols[i % 3].markdown(f"<div style='background-color: #f0f0f0; border-radius: 5px; padding: 10px; margin: 5px; color: black;'>- {comment}</div>", unsafe_allow_html=True)
else:
    st.write("No hay comentarios aún. ¡Sé el primero en comentar!")

# Estilo adicional con CSS
st.markdown("""
<style>
    .stTextInput > div > input {
        font-size: 16px;
        padding: 10px;
    }
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
