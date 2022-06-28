import pandas as pd
from pandas import read_csv
import csv

calles_file = "data/Lima-calles.csv"
intersection_file = "data/Lima-intersecciones.csv"

columns = ['id', 'name', 'intersection_count']


def calles():
    calles_df = read_csv(calles_file, sep=";", header=None, names=columns)
    # print(calles_df)
    return calles_df



# read csv file calles_file  colum 'Plaza 2 de Mayo' and save in a list
def calles_list():
    calles_df = read_csv(calles_file, sep=";", header=None, names=columns)
    calles_list = calles_df['name'].tolist()
    return calles_list



def intersc():
    columns = ['id', 'calle_id', 'cale_name', 'start_id', 'end_id', 'int_start_id', 'int_end_id', 'distancia',
               'velocidad', 'costo', 'costo_inverso', 'start_lat', 'start_log', 'end_lat', 'end_log']
    intersc_df = pd.read_csv(intersection_file, sep=";", header=None, names=columns)

    # print(intersc_df)
    return intersc_df
