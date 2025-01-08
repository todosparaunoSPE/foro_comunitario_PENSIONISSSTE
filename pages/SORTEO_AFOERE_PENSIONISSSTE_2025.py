# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:44:14 2025

@author: jperezr
"""

import streamlit as st
import os

# Archivo donde se guardarán los comentarios
comments_file = 'experiencias.txt'

# Función para cargar comentarios desde el archivo de texto
def load_comments():
    if os.path.exists(comments_file):
        with open(comments_file, 'r') as f:
            return f.readlines()  # Lee todas las líneas del archivo
    return []

# Función para guardar un nuevo comentario en el archivo de texto
def save_comment(comment):
    with open(comments_file, 'a') as f:  # Abre el archivo en modo "append"
        f.write(comment + '\n')  # Añade el comentario seguido de una nueva línea

# Título de la aplicación
st.set_page_config(page_title="Foro Comunitario de Pensionissste", page_icon="💬", layout="wide")
st.title("💬 Foro Comunitario de Pensionissste")
st.markdown("¡Bienvenidos al foro de PENSIONISSSTE! Este es un espacio creado para que puedas compartir tus experiencias, resolver dudas y aprender más sobre cómo aprovechar al máximo tu ahorro para el retiro.")

# Cargar comentarios existentes
if 'comments' not in st.session_state:
    st.session_state.comments = load_comments()

# Función para agregar un nuevo comentario
def add_comment():
    comment = st.session_state.new_comment
    if comment:
        st.session_state.comments.append(comment)  # Agrega el comentario al estado
        save_comment(comment)  # Guarda el comentario en el archivo
        st.session_state.new_comment = ""  # Limpia el campo de entrada

# Formulario para agregar comentarios
st.subheader("👉 Cuéntanos un poco sobre tu experiencia con el sistema de pensiones:")
comment_input = st.text_input("Comentario:", key='new_comment', on_change=add_comment)

# Mostrar comentarios
st.subheader("Comentarios:")
if st.session_state.comments:
    for comment in st.session_state.comments:
        st.markdown(f"- {comment.strip()}")  # Muestra el comentario sin espacios en blanco
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
