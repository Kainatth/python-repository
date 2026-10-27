import csv

rows = [
    ["emp_id", "name", "salary", "department"],
    [1, "Ravi", 55000, "IT"],
    [2, "Sita", 62000, "HR"],
    [3, "Arjun", 75000, "IT"],
    [4, "Lakshmi", 48000, "Finance"]
]

with open("employee_small.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("CSV file created")