import csv

with open("employee_small.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

        import pandas as pd

        df = pd.read_csv("employee_small.csv")
        print(df)