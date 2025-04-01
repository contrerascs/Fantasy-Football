import pandas as pd

def clean_data(week):
    input_file = f"data/data_csv/qb_fantasy_week_{week}.csv"
    output_file = f"data/data_csv/qb_fantasy_week_{week}.csv"

    df = pd.read_csv(input_file)

    # Eliminar la primer fila del DataFrame
    df = df.drop(0,axis=0)
    print(df)


clean_data(1)