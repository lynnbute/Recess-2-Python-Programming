# Dictionaries are used to store data values in key value pairs.
# they are ordered, changeable and dont allow duplicates. 
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
print(dict)

# we can also print specific values from a dictionary.
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
print(dict["brand"])

# duplicate values will overwrite existing values
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964",
    "year" : "2020" # 2020 will be printed instead of 1964
}
print(dict)

#dictionary length
print(len(dict))

# Type
print(type(dict))

# the dict() constructor
# Using dictionary constructor to create a dictionary
"""person = dict{name="John", age=25, city="New York"}
# Print the created dictionary
print(person)"""


# Access dictionary items
# we can access items in a dictionary by referring to its key name.
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
x = dict["model"]
x = dict.get("model")

# Get keys
# the keys() method will return a list of all the keys in the dictionary.
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

y = dict.get("model")
print(y)

# change values
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
dict["year"] = 2018
#the clear() empties the dictionary

                                   #EXERCISES
# Exercise 1: use the values method to return a list of all values in the dictionary.
# Dictionary with some key-value pairs
person = {
    'name': 'John', 'age': 25, 'city': 'New York'}

# Get a list of all values in the dictionary
values_list = list(person.values())

# Print the list of values
print(values_list)

# Exercise 2: use the values method to check if a key does exist in your dictionary
# Check if a key exists in the dictionary
key = 'age'
if key in person.keys():
    print(f"The key '{key}' exists in the dictionary.")
else:
    print(f"The key '{key}' does not exist in the dictionary.") 
       
# Exercise 3: give an example on how to change dictionary items, how to update
# Dictionary with some key-value pairs
person = {'name': 'John', 'age': 25, 'city': 'New York'}
# Change a specific item in the dictionary
person['age'] = 30
# Print the updated dictionary
print(person)
# Update the dictionary with new key-value pairs
person.update({'occupation': 'Engineer', 'city': 'San Francisco'})
# Print the updated dictionary
print(person)

# Exercise4 give an example on how to add dictionary items, how to remove dictionary items
 # Add dictionary items
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
dict["color"] = "red"
print(dict)

 #remove items from the dictionary
#we use pop() to remove items
# the popitem() removes the last inserted item, in versions before 3.7, a random item is removed instead.
dict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : "1964"
}
dict.pop("model")
print(dict)

#Exercise5 give an example on how you can loop through a dictionary and also how to nest dictionaries
 #Loop through a dictionary
for x in dict:
    print(x)
    
for x, y in dict.items():
    print(x, y)
    
 # nested dictionaries
family = {
    "child1" : {
        "name" : "Emmy",
        "year" : "2004"
    },
    "child2" : {
        "name" : "Toby",
        "yaer" : "2001"
    }
} 

# access items in a nested dictionary
print(family["child2"]["name"])    
print(family["child1"]["year"])    

