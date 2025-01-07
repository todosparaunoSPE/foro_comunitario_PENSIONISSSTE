# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:44:14 2025

@author: jperezr
"""

import streamlit as st
import sqlite3

# Conexión a la base de datos SQLite
def create_connection():
    conn = sqlite3.connect('sorteo.db')
    return conn

# Crear tabla si no existe
def create_table():
    conn = create_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comment TEXT NOT NULL
            )
        ''')
    conn.close()

# Función para cargar comentarios desde la base de datos
def load_comments():
    conn = create_connection()
    with conn:
        comments = conn.execute('SELECT comment FROM comments').fetchall()
    return [comment[0] for comment in comments]

# Función para guardar un nuevo comentario en la base de datos
def save_comment(comment):
    conn = create_connection()
    with conn:
        conn.execute('INSERT INTO comments (comment) VALUES (?)', (comment,))
    conn.close()

# Crear tabla al inicio
create_table()

# Configuración de la aplicación
st.set_page_config(page_title="Foro Comunitario de Pensionissste - Sorteo 2025", page_icon="💬", layout="wide")
st.title("💬 Foro Comunitario de AFORE PENSIONISSSTE - Sorteo 2025")
st.markdown("¡Bienvenidos al foro de PENSIONISSSTE!")

# Cargar comentarios existentes
if 'comments' not in st.session_state:
    st.session_state.comments = load_comments()

# Función para agregar un nuevo comentario
def add_comment():
    comment = st.session_state.new_comment
    if comment:
        save_comment(comment)  # Guardar en la base de datos
        st.session_state.comments.append(comment)  # Agregar al estado
        st.session_state.new_comment = ""

# Preguntas y comentarios
st.subheader("👉 Deja tus comentarios o preguntas:")
comment_input = st.text_input("Comentario:", key='new_comment', on_change=add_comment)

# Mostrar comentarios
st.subheader("Comentarios:")
if st.session_state.comments:
    for comment in st.session_state.comments:
        st.markdown(f"- {comment}")
else:
    st.write("No hay comentarios aún.")
