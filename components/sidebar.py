import streamlit as st

def render_sidebar(df):
    # Renderiza la barra lateral completa.
    with st.sidebar:
        st.image('assets/logo.png', use_container_width=True)

        # Obtener lista de temporadas ordenadas (más recientes primero)
        week_list = sorted(df["Week"].unique().tolist(), reverse=True)
        
        # Selección de temporada primero
        selected_season = st.selectbox('Select a season', week_list, key='season')
        
        # Filtrar el dataframe por la temporada seleccionada
        season_df = df[df["Week"] == selected_season]
        
        # Obtener lista de QBs que jugaron en esa temporada
        qb_list = season_df["Player"].unique().tolist()
        
        # Selección del primer QB
        selected_qb = st.selectbox("Select a quarterback", qb_list)

    return selected_qb, selected_season