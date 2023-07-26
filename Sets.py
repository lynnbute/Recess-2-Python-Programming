#Sets store multiple items in a single variable, are unordered and dont allow duplicates
#they are inbuilt datatypes, more like tuples
#they are unchangeable but one can add and remove items

set_one = {"Rice", "Matooke", "Irish"}
#print(set_one)

#duplicates in sets
set_one = {"Rice", "Matooke", "Irish", "Rice"}
print(set_one) #it will not print the last Rice

#Set Length, data types, accessing items in a set, add items, add 2 sets together

students = {"Timothy", "Doreen", "Lynatte", "Willy", "Adam", "Sam", "Eric"}
print(len(students))

#Data types
students = {"Timothy", "Doreen", "Lynatte", "Willy", "Adam", "Sam", "Eric"}
print(type(students))

#Accessing items in a set
#You cannot access sets using index or key, so we use the for loop
students = {"Timothy", "Doreen", "Lynatte", "Willy", "Adam", "Sam", "Eric"}
for y in students:
    print(y)
    
#We can also use the in keyword to see if a specified item is found in the set
students = {"Timothy", "Doreen", "Lynatte", "Willy", "Adam", "Sam", "Eric"}
print("Willy" in students)  

#Add items in a set
#We use the add() method
students = {"Timothy", "Doreen", "Lynatte", "Willy", "Adam", "Sam", "Eric"} 
students.add("Molly")
print(students)

#Add 2 sets together
#To add 2 sets together, we use the update() method
fruits = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

fruits.update(tropical)

print(fruits)

