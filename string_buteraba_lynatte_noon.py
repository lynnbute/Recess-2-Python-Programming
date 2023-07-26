# represented by "" or ''
print("morning")
print('morning')

#Assign a string to a variable
w = "afternoon"
print(w)

#Multiline strings
t= """ i am offering BSSE year 3
Currently doing recess in python,
Data science, Django."""
print(t)

# strings as arrays
a = "Afternoon"
print(a[1])

#Exercise1 use the len() function to determine the length of your string
# String
string = "Hello, Universe!"
# Determine the length of the string
length = len(string)
# Print the length
print("Length of the string:" , length)

# Exercise2 give an example of using a for loop in a string
my_string = "Hello, Universe!"
# Iterate over each character in the string using a for loop
for char in my_string:
    print(char)

# Exercise3 give an example of slicing in strings
my_string = "Hello, World!"
# Slicing the string
slice1 = my_string[7:12]  # Extracts "World"
slice2 = my_string[:5]    # Extracts "Hello"
slice3 = my_string[7:]    # Extracts "World!"
# Print the slices
print(slice1)
print(slice2)
print(slice3)

# How to modify strings
a = "Afternoon"
print(a.lower())
print(a.upper())

# remove whitespace
b = " After noon "
print(b.strip())

#string concantenation
c= "Afternoon"
d = "class"
w = c + d
print(w)