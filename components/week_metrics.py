import streamlit as st
import pandas as pd
import numpy as np

def week_fantasy_points(week_data, selected_qb):
    week = week_data['Week'].iloc[0]
    st.header(f'{selected_qb} fantasy points in Week {week}')

    player = week_data[week_data['Player'] == selected_qb]

    c1, c2, c3, c4, c5 = st.columns(5)

    titulos = {
        'Att':'Atts',
        'Cmp':'Completes',
        'Yds': 'Air Yds',
        'TD':'Touchdowns',
        'Int':'Interceptions',
    }

    # Mostrar estadísticas de la temporada
    stats = ["Att", "Cmp", "Yds", "TD", "Int"]
    columns = st.columns(len(stats))

    for col, stat in zip(columns, stats):
        with col:
            st.metric(label=titulos[stat], value=player[stat],border=True)

    st.dataframe(week_data)
