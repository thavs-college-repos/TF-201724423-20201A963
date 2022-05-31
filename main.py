import csv

result = []
file = open("data\\Lima-calles.csv")
reader = csv.reader(file, delimiter=';')
for row in reader:
    print(row)

# with open('data\Lima-calles.csv', newline='') as File:
#     reader = csv.DictReader(File)
#     for row in reader:
#         result.append(row)
#     print(result)
