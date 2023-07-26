# Exercise 1 (Lists)
#1. 
names = ["Livingstone", "Adam", "Rose","Ruth","Tina"]
print(names[1])

#2
names[0] = "Lynatte"
print(names)

#3
names.append("Samuel")
print(names)

#4
names[2] = "Bathel"
print(names)

#5
names.remove("Ruth")
print(names)

#6
print(names[-1])

#7
fruits = ["mango", "apple", "banana","grape", "pear", "strawberry", "pineapple"]
print(fruits[2:5])

#8
countries = ["Uganda", "USA", "Nepal","Kenya","Canada"]
countries_copy = countries[:]
print("Original List:", countries)
print("Copied List:", countries_copy)

#9
for x in countries:
    print(x)
    
#10
animals = ["Lion", "Elephant", "Tiger", "Giraffe", "Monkey"]
ascending_order = sorted(animals)
descending_order = sorted(animals, reverse=True)
print("Original List:", animals)
print("Ascending Order:", ascending_order)
print("Descending Order:", descending_order)

#11
animal_names_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("Animal Names with 'a':", animal_names_with_a)

#12
first_names = ["Lynatte", "Joanitta", "Irene"]
last_names = ["Buteraba", "Bangi", "Aloya"]
new_list = first_names + last_names
print(new_list)

# Exercise 2(Tuples)
#1.
x = ("samsung", "iphone","tecno", "redmi")
favorite_brand = "samsung"
if favorite_brand in x:
    print("My favorite phone brand is", favorite_brand)
else:
    print("My favorite phone brand is not in the list")
    
#2
print(x[-2])

#3
x_list = list(x)
x_list[1] ="itel" 
x = tuple(x_list)
print(x)

#4
x = ("samsung", "iphone","tecno", "redmi")
s = list(x)
s.append("Huawei")
print(s)
x = tuple(s)
print(x)

#5 Write a python program to loop through the tuple above.
for item in x :
    print (item)
    
#6  Write a python program to remove/delete the first item in your tuple.
x_list = list(x)
x_list.pop(0)
x_updated = tuple(x_list)
print("Updated Tuple:", x_updated)

#7 Using the tuple() constructor, create a tuple of the cities in Uganda.
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print("Cities in Uganda:", cities)

#8 Write a python program to unpack your tuple
city1, city2, city3, city4, city5 = cities
print("City 1:", city1)
print("City 2:", city2)
print("City 3:", city3)
print("City 4:", city4)
print("City 5:", city5)

#9  Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
print(cities[1:4])

#10 Write two tuples, one containing your first names and the other your second names. Join
#the two tuples
first_names = ("Lynatte", "Joanitta", "Irene")
last_names = ("Buteraba", "Bangi", "Aloya")
new_tuple = first_names + last_names
print("Joined tuple", new_tuple)

#11 Create a tuple of colors and multiply it by 3.
colors = ("red", "blue", "green")
multiplied_colors = colors * 3
print("Multiplied Colors:", multiplied_colors)

#12 Return the number of times 8 appears in this tuple
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count= this_tuple.count(8)
print("Number of times 8 appears:", count)

# Exercise 3
# 1 Use the set() constructor to create a set of 3 of your favorite beverages.
beverages = set(["water", "tea", "juice"])
print("Favorite Beverages Set:", beverages)

#2 Use the correct method to add 2 more items to the beverages set.
beverages = {"water", "tea", "juice"}
beverages.update(["soda", "smoothie"])
print("Updated Beverages Set:", beverages)

# 3 Given the set below;
mySet = {"oven", "kettle", "microwave", "refrigerator"}
#Check if microwave is present in the set
if "microwave" in mySet:
    print("The item 'microwave' is present in the set")
else:
    print("The item 'microwave' is not present in the set")
    
#4 Write a python program to remove “kettle” from the set above.
mySet.remove("kettle")
print("Updated Set:", mySet)
 
#5 Write a python program to loop through the set above
for x in mySet:
    print(x)
       
#6 Write a set of 4 items and a list of two items. Write a python program to add elements in
#the list to elements in the set.  
mySet = {"apple", "banana", "orange", "grape"}
myList = ["strawberry", "melon"]
mySet.update(myList)
print("Updated Set:", mySet)

#7 Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {12, 3, 5}
first_names = {"Alex", "Bobby", "Sam"}
joined_set = ages.union(first_names)
print("Joined Set:", joined_set)

# Exercise 4
#1 Declare two variables, an integer and a string and use the correct method to concatenate
#the two variables.
string = "Hello"
integer = 10
concatenated_variable = string + str(integer)
print("Concatenated Variable:", concatenated_variable)

#2 Consider the example below;
txt = " Hello, Uganda! "
#Output the string without spaces at the beginning, in the middle and at the end.
txt = txt.strip()
replaced = txt.replace(" ", "")
print(replaced)

#3Write a python program to convert the value of ‘txt’ to uppercase.
uppercase_txt = txt.upper()
print("Uppercase Text:", uppercase_txt)

# 4 Write a python program to replace character ‘U’ with ‘V’ in the string above.
updated = txt.replace('U', 'V')
print("Updated Text:", updated)

# 5 Using the code below, write a python program to return a range of characters in the 2nd, 3rd and 4th position
y = "I am proudly Ugandan"
print(y[1:4])

# 6 The piece of code below will give an error when output;
x = "All “Data Scientists” are cool!"
#Write a python program to correct it.
x = "All \"Data Scientists\" are cool!"
print(x)

# Exercise 5
# 1. With reference to the dictionary below, write a python program to print the value of the shoe size
#Add this dictionary to your .py file
Shoes = {
"brand" : "Nick",
"color" : "black",
"size" : 40
}
shoe_size = Shoes["size"]
print("Shoe Size:", shoe_size)

#2. Write a python program to change the value “Nick” to “Adidas”
Shoes["brand"] = "Adidas"
print("Updated Shoes Dictionary:", Shoes)

# 3 Write a python program to add a key/value pair "type”: "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("Updated Shoes Dictionary:", Shoes)

# 4 Write a python program to return a list of all the keys in the dictionary above.
keys_list = list(Shoes.keys())
print("List of Keys:", keys_list) 
 
# 5 Write a python program to return a list of all the values in the dictionary above.
values_list = list(Shoes.values())
print("List of Values:", values_list)

# 6 Check if the key “size” exists in the dictionary above.
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")
    
# 7     Write a python program to loop through the dictionary above
for key, value in Shoes.items():
    print("Key:", key)
    print("Value:", value)
    print("---")
    
# 8 Write a python program to remove “color” from the dictionary.    
del Shoes["color"]
print("Updated Shoes Dictionary:", Shoes)

# 9 Write a python program to empty the dictionary above.
Shoes.clear()
print("Empty Shoes Dictionary:", Shoes)

# 10 Write a dictionary of your choice and make a copy of it   
original_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
copied_dict = dict(original_dict)
print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

# 11 . Write a python program to show nested dictionaries
student = {
    "name": "John",
    "age": 20,
    "grades": {
        "math": 90,
        "science": 85,
        "history": 95
    },
    "contact": {
        "email": "john@example.com",
        "phone": "1234567890"
    }
}
print("Name:", student["name"])
print("Age:", student["age"])
print("Math Grade:", student["grades"]["math"])
print("Email:", student["contact"]["email"])


  
