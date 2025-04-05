import streamlit as st
import pandas as pd
import numpy as np

def rank_in_stat(week_data,player,stat):
    player_data = week_data[week_data['Player'] == player]
    metric = player_data[stat].sum()

    titulos = {
        'Att':'Atts',
        'Cmp':'Completes',
        'Yds': 'Air Yds',
        'TD':'Touchdowns',
        'Int':'Interceptions',
        'Pts*':'Total Pts'
    }   

    week_data = week_data.sort_values(by=stat, ascending=False).reset_index(drop=True)
    week_data[stat + "_rank"] = week_data[stat].rank(method="min", ascending=False)
    rank = week_data.loc[week_data["Player"] == player, stat + "_rank"].values[0]

    if stat == 'Int':
        if rank > 20:
            st.metric(titulos[stat], f"{metric}", f"{(int(rank))}º",border=True)
        elif rank > 10:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º", "off",border=True)
        else:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º","inverse",border=True)
    else:
        if rank > 20:
            st.metric(titulos[stat], f"{metric}", f"{(int(rank))}º","inverse",border=True)
        elif rank > 10:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º", "off",border=True)
        else:
            st.metric(titulos[stat], f"{metric}", f"{int(rank)}º",border=True)

def week_fantasy_points(week_data, selected_qb):
    week = week_data['Week'].iloc[0]
    st.header(f'{selected_qb} fantasy points in Week {week}')

    # Mostrar estadísticas de la temporada
    stats = ['Pts*',"Att", "Cmp", "Yds", "TD", "Int"]
    columns = st.columns(len(stats))

    for col, stat in zip(columns, stats):
        with col:
            rank_in_stat(week_data,selected_qb,stat)

    st.dataframe(week_data)
