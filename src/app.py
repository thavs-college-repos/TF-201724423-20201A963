import pandas as pd

street_file = "data/Lima-calles.csv"
intersection_file = "data/Lima-intersecciones.csv"


def index() -> None:
    columns = ['id', 'name', 'intersection_count']
    df = pd.read_csv(street_file, sep=';', header=None, names=columns)
    print(df)

# def index():
#     result = []
#     file = open("./data/Lima-calles.csv")
#     reader = csv.reader(file, delimiter=';')
#     for row in reader:
#         print(row)

# with open('data\Lima-calles.csv', newline='') as File:
#     reader = csv.DictReader(File)
#     for row in reader:
#         result.append(row)
#     print(result)
