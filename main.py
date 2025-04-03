import streamlit as st

from components.sidebar import render_sidebar
from helpers.data_loader import load_dataset
from components.week_metrics import week_fantasy_points

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
week_data = df[df['Week'] == selected_week]

# Verificar si los jugadores están en la temporada seleccionada
qb_exists = selected_qb in week_data['Player'].values

if not qb_exists:
    # Mostrar advertencias si un jugador no jugó en la semana seleccionada
    if not qb_exists:
        st.warning(f"⚠️ {selected_qb} not played in week {selected_week}.")
else:
    # Mostrar puntos fantasy si el jugador seleccionado si jugó esa semana
    week_fantasy_points(week_data,selected_qb)