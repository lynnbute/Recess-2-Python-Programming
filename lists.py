#Lists are used to store multiple items in a single variable.
#Lists are ordered, changeable, allows for duplicate values.
Afternoon = ["Lynatte", "Prossie", "Agatha"]
print(Afternoon)

#Duplicates in lists
Afternoon = ["Lynatte", "Prossie", "Agatha", "Lynatte", "Agatha"]
print(Afternoon)

#List length
print(len(Afternoon))

#Type
print(type(Afternoon))

#Access List items
print(Afternoon[1])
print(Afternoon[4])

#Negative indexing
print(Afternoon[-2])
print("My name is" + " " + Afternoon[-3])

#Accessing elements in a range
print(Afternoon[2:4])
print(Afternoon[:4]) # item on index 5 will not be output
print(Afternoon[1:]) #items at index 0 will not be printed

#Add elements in the lists
Afternoon.append("Ruth")
print(Afternoon)

#inserting items
Afternoon.insert(0, "Will")
print(Afternoon)

#Extend list elements
#To append elements from another list to the current list, use the extend() method.
Afternoon = ["Lynatte", "Prossie", "Agatha"]
Morning = ["Jeff", "Livingstone"]
Afternoon.extend(Morning)
print(Afternoon)

#Removing items
Afternoon.remove("Agatha")
print(Afternoon)

#Join 2 lists
Afternoon = ["Lynatte", "Prossie", "Agatha"]
Morning = ["Jeff", "Livingstone"]
new_list = Afternoon + Morning
print(new_list)
