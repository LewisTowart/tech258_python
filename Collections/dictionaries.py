# Dictionaries

# key = value pairs
# key is the reference, value is the data storage mechanism (int, string, etc.)

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up", "collections"]
}

print(student1["stream"])
print(student1["completed_lesson_names"][0])
# Changing the value of a key
student1["completed_lessons"] = 3
print(student1["completed_lessons"])
# Removing an item from a list in a dictionary
student1["completed_lesson_names"].remove("collections")
print(student1["completed_lesson_names"])

# getting the keys for a dictionary
print(student1.keys())

