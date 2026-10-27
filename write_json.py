import json

data = {
    "name": "Kaiinatth",
    "age": 22,
    "skills": ["Python", "SQL", "Git"]
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created")