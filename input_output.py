# Input and output in python
# input('prompt)

# Example of input
name = input("Enter your name:  ")  # asks for the user's name
print("My name is, " + name)

# example 2
number = int(input("Enter a value: "))
product = number * 10
print(product)

# multiple inputs in python
s, r, w = map(int, input("Enter the values: ").split())
print("The values are: ", end="")
print(s, r, w)

# How to capture input from a tuple
w = (2, 4, 6, 5, 8)
print("Current Tuple")
print(w)

E = list(w)
E.append(int(input("Enter a value: ")))
w = tuple(E)
print("Updated tuple")
print(w)

my_list = list(map(int, input("Enter the list values: ").split()))
my_set = set(map(int, input("Enter the set values: ").split()))
print(my_list)
print(my_set)
