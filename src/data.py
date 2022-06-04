import pandas as pd
from pandas import read_csv

calles_file = "data/Lima-calles.csv"
intersection_file = "data/Lima-intersecciones.csv"


def calles():
    columns = ['id', 'name', 'intersection_count']
    calles_df = read_csv(calles_file, sep=";", header=None, names=columns)
    # print(calles_df)
    return calles_df


def intersc():
    columns = ['id', 'calle_id', 'cale_name', 'start_id', 'end_id', 'int_start_id', 'int_end_id', 'distancia',
               'velocidad', 'costo', 'costo_inverso', 'start_lat', 'start_log', 'end_lat', 'end_log']
    intersc_df = pd.read_csv(intersection_file, sep=";", header=None, names=columns)

    # print(intersc_df)
    return intersc_df
