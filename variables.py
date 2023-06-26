#variables are containers for storing data. 
"""python has no command for declaring a variable, it is created the moment you first
assign a value to it."""

x = 4
x = "Sally"
print(x)

#if you want to specify the data-type of a variable, we use casting.
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

# you can get the datatype of a variable using the type() function
x = 5
y = "John"
print(type(x))
print(type(y))