import csv

FILE_PATH = "PyBank/Resources/budget_data.csv"
data = []

def read_data():
    with open(FILE_PATH, newline="") as file:
        csv_reader=csv.reader(file)
        next(csv_reader,None)

        for row in csv_reader:
            data.append(row)
read_data()      
print(data)



