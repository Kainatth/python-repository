import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(type(data))
print("Name:", data["name"])
print("First skill:", data["skills"][0])
