# Group blocks of code. There is need for clean, reusable and maintainable code.
def afternoon():
    print("Class starts at 2")
    print("Attendees are close to 100")

# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
# Example


def myfunction():
    pass


# calling a function
afternoon()
# Arguements and Parameters
# Parameters


def afternoon(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


# Default Parameter Value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()

# using return


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
