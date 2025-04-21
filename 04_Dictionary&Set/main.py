names = {"person1": "Afzaal", "person2": "Ijaz", "person3": "Ansari", "totalPerson": 3}

print(names, type(names)) 

print(names["person1"])  # it will return the value of key

names.update(
    {"person1": "Talha ", "person4": "Fardeen"}
)  # in dictionary we can update the value of key and also add new key value pair its awesome

print(" updated dictionary :", names)
print(names.items())  # it will return all key value pair in tuple
print(names.keys())  # it will return all keys
print(names.values())  # it will return all values
print(len(names))  # it will return the length of dictionary


print(names.get("person1"))  # it will return the value of key
print(names["person1"])  # it will return the value of key
# but the difference between get and [] is that if key is not present in dictionary then get will return None but [] will give error


names.clear()  # it will clear the dictionary

names.copy()  # it will return the copy of dictionary

names.pop("person1")  # it will remove the key value pair from dictionary
names.popitem()  # it will remove the last key value pair from dictionary
print(names)