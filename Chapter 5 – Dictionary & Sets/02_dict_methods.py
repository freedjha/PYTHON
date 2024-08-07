marks = {
    "key": "value",
    "harry": 100,
    "shiv": 23,
    "Ram" : 24
}

# print(marks.items()) #Returns a list of (key,value)tuples

# print(marks.keys())
# print(marks.values())

marks.update({"harry": 99, "Renu": 100})
print(marks)
print(marks.get("Harry2")) # Prints None
print(marks["Harry2"]) # Returns an error
print(marks.get("harry")) # Prints None