import streamlit as st

from components.sidebar import render_sidebar
from helpers.data_loader import load_dataset

# Configuración inicial de Streamlit
st.set_page_config(
    page_title='Fantasy Football',
    page_icon=':football:',
    layout='wide',
    initial_sidebar_state='expanded',
)

df = load_dataset()
selected_qb, selected_week = render_sidebar(df)

# Filtrar DataFrame por la temporada seleccionada
df_season = df[df['Week'] == selected_week]

# Verificar si los jugadores están en la temporada seleccionada
qb1_exists = selected_qb in df_season['Player'].values

if not qb1_exists:
    # Mostrar advertencias si un jugador no jugó en la temporada seleccionada
    if not qb1_exists:
        st.warning(f"⚠️ {selected_qb} not played in week {selected_week}.")
else:
    # Mostrar comparación solo si ambos jugadores jugaron en la temporada seleccionada
    pass