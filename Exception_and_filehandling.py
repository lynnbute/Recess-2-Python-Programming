"""
Exception handling in Python allows you to  handle and recover from errors.

In Python, it done using the try, except, else, and finally blocks.

try block: It encloses the code that may raise an exception.

except block: It specifies the type of exception to catch and the code to be executed when that exception occurs.

else block: It is optional and executes if no exceptions occur in the try block.

finally block: It is also optional and executes regardless of whether an exception occurred or not. """
# Key error
import os
my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]  # Trying to access a key that doesn't exist
    print(value)
except KeyError:
    print("Error: Key not found")
finally:
    print("Iam always executed")


# Zero division error
try:
    result = 10 / 0  # Attempting to divide by zero
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
finally:
    print("Iam always executed")

# Index error
my_list = [1, 2, 3]

try:
    value = my_list[3]  # Trying to access an index that is out of range
    print(value)
except IndexError:
    print("Error: Index out of range")
finally:
    print("Iam always executed")

# Name error
# occurs when a local or global name is used but cannot be found within the current scope.
result = sum([1, 2, 3])  # No error, correct usage
print(Result)  # NameError: name 'Result' is not defined


# ValueError: This exception is raised when a method is called with an invalid argument
# such as trying to convert a string to an integer
try:
    number = int("abc")  # Trying to convert a non-numeric string to an integer
    print(number)
except ValueError:
    print("Error: Invalid value")

# IOError: This exception is raised when an I/O operation fails due to an input/output error.
try:
    # Trying to open a nonexistent file
    file = open("nonexistent_file.txt", "r")
    content = file.read()
    file.close()
    print(content)
except IOError:
    print("Error: File not found or cannot be opened")

# ImportError: This exception is raised when an import statement fails to find or load a module
try:
    import nonexistent_module
except ImportError:
    print("Error: Module not found or cannot be imported")

# File handling allows us perform operations such as reading from files, writing to files, appending data, and more.
# Opening a file:
# file = open("filename.txt", "r")

# Reading from a file:
# content = file.read()

# Writing to a file:
"""file = open("filename.txt", "w")
file.write("We are in the afternoon session")
"""
# Closing a file:
# file.close()
# we also use with statement which automatically takes care of closing the file for you.
# Example
# Create a file
with open("myfile.txt", "w") as file:
    file.write("This is a new file.")

# Open and read from a file
with open("myfile.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# Write to a file
with open("myfile.txt", "w") as file:
    file.write("This is the modified content.")

# Append to a file
with open("myfile.txt", "a") as file:
    file.write("\nThis is appended content.")

# Open and read from the modified file
with open("myfile.txt", "r") as file:
    content = file.read()
    print("Modified file content:", content)

"""  # Delete the file
os.remove("myfile.txt")
print("File deleted.")"""
