# Dictionaries

# Key Value pairs
# Create a dictionary
Student_1 = {
    "name" : "Susan",
    "stream" : "DevOps",
    "completed_lessons" : 4,
    "completed_lesson_names" : ["varaibles", "data_types", "github"]
}

# Access data in dictionary
print(Student_1["stream"])
print(Student_1["completed_lesson_names"][0])

# Updating values in a dictionary
Student_1["completed_lessons"] = 3
print(Student_1["completed_lessons"])

# Remove values from a dictionary
Student_1["completed_lesson_names"].remove("data_types")
print(Student_1["completed_lesson_names"])

# Dictionary methods
print(Student_1.keys()) # Keys
print(Student_1.get("name")) # Get value from a key

# Get the values of a dictionary
print(Student_1.values())
print(Student_1.items())


