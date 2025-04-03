import streamlit as st

def week_fantasy_points(week_data, selected_qb):
    week = week_data['Week'].iloc[0]
    st.header(f'{selected_qb} fantasy points in Week {week}')

    player = week_data[week_data['Player'] == selected_qb]

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    with c1:
        st.metric(label='Fantasy Points', value=player['Pts*'],border=True)

    st.dataframe(week_data)
