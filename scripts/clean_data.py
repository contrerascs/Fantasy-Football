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

    # Convertir columnas numéricas
    qb_complete = qb_complete.apply(pd.to_numeric, errors='ignore')

    # Guardar el DataFrame consolidado en un nuevo archivo CSV
    qb_complete.to_csv('data/qb_fantasy_football.csv', index=False)


clean_data()