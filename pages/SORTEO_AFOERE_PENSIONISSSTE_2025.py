# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:44:14 2025

@author: jperezr
"""

import streamlit as st
import sqlite3

# Conexión a la base de datos SQLite
def create_connection():
    conn = sqlite3.connect('comentarios.db')
    return conn

# Crear tabla si no existe
def create_table():
    conn = create_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS comentarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comentario TEXT NOT NULL
            )
        ''')
    conn.close()

# Función para cargar comentarios desde la base de datos
def load_comments():
    conn = create_connection()
    with conn:
        comentarios = conn.execute('SELECT comentario FROM comentarios').fetchall()
    return [comentario[0] for comentario in comentarios]

# Función para guardar un nuevo comentario en la base de datos
def save_comment(comentario):
    conn = create_connection()
    with conn:
        conn.execute('INSERT INTO comentarios (comentario) VALUES (?)', (comentario,))
    conn.close()

# Crear tabla al inicio
create_table()

# Configuración de la aplicación
st.set_page_config(page_title="Foro Comunitario de Pensionissste", page_icon="💬", layout="wide")
st.title("💬 Foro Comunitario de Pensionissste")
st.markdown("¡Bienvenidos al foro de PENSIONISSSTE!")

# Cargar comentarios existentes
if 'comments' not in st.session_state:
    st.session_state.comments = load_comments()

# Función para agregar un nuevo comentario
def add_comment():
    comentario = st.session_state.new_comment
    if comentario:
        save_comment(comentario)  # Guardar en la base de datos
        st.session_state.comments.append(comentario)  # Agregar al estado
        st.session_state.new_comment = ""
        st.success("Comentario agregado exitosamente.")
    else:
        st.warning("El comentario no puede estar vacío.")

# Formulario para agregar comentarios
st.subheader("👉 Cuéntanos un poco sobre tu experiencia con el sistema de pensiones:")
comment_input = st.text_input("Comentario:", key='new_comment', on_change=add_comment)

# Mostrar comentarios
st.subheader("Comentarios:")
if st.session_state.comments:
    for comentario in st.session_state.comments:
        st.markdown(f"- {comentario}")
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
