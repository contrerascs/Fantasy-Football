import pandas as pd

def clean_data():
    # Lista para almacenar los DataFrames
    qb_dataframes = []
    for week in range(1,19):
        input_file = f'data/data_csv/qb_fantasy_week_{week}.csv'
        df = pd.read_csv(input_file,skiprows=1)
        df['Week'] = f'{week}'
        # Agregar el DataFrame a la lista
        qb_dataframes.append(df)

    # Unir todos los DataFrames en uno solo
    qb_complete = pd.concat(qb_dataframes, ignore_index=True)

    qb_complete = qb_complete.drop(columns={'TD.3'})

    # Renombrar columnas
    qb_complete = qb_complete.rename(columns={'Att.1': 'Rush_Att', 'Yds.1': 'Rush_Yds', 'TD.1': 'Rush_TD', '2Pt.1':'Rush_2Pt',
                            'Yds.2': 'Rec_Yds', 'TD.2': 'Rec_TD', '2Pt.2': 'Rec_2Pt',})

    # Guardar el DataFrame consolidado en un nuevo archivo CSV
    qb_complete.to_csv('data/qb_fantasy_football.csv', index=False)


clean_data()