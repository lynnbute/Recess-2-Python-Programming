# Advanced topics in python
"""
Regular expressions
Generators and iterators
Decorators
Context managers
Multithreading and multiprocessing
"""
"""Regular expressions

\d matches any digit (0-9)
\w matches any alphanumeric character (A-Z, a-z, 0-9, underscores)
\s matches any whitespace character
* matches 0 or more occurrences of preceding characters or group
+ matches one or more occurrences of preceding characters or group
? matches zero or one occurrences of preceding characters or group
. matches any character except a new line
[] matches any character within the square bracket
[^] matches any character not within the square bracket
$ matches the end of line
^ matches the start of line
\b matches a line break
"""
# Matching and searching
# regex re.match(), re.search(), re.findall()
# Example 1 Demonstrating regex | match first word, match group word, match all numbers
import time
import re

text = "Hello, my name is Lynatte Joanitta. I am a programmer with 10 years experience"

# Match first word
match = re.search(r"\b\w+\b", text)
if match:
    print("Match:", match.group())

# Matching numbers
matches = re.findall(r"\d+", text)
print("Matches: ", matches)

# Example2 validate email format/address


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return True
    else:
        return False


# Example usage
email1 = "jeff.geoff98@gmail.com"
email2 = "jeff.geoff98@gmailcom"
print(validate_email(email1))
print(validate_email(email2))

# Generators and iterators
# 'yield' generator
# Iterator '__iter__'"__next__"iterator


def factorial(n):
    # Return the factorial of a number
    if n == 0:
        yield 1
    else:
        # yield n * factorial(n - 1)
        fact = 1
        for i in range(1, n + 1):
            fact *= i
            yield fact


# Print the factorial of a number from 1-10
for i in range(1, 10):
    print(*factorial(i))

# Example3
# Generate a function that yields the square of a number from 1-10


def squares():
    for i in range(1, 10):
        yield i**2


# Create an iterator object that yields the sq of numbers 1-10
squares_iterator = squares()
for i in range(5):
    print(next(squares_iterator))

# Decorators @my_decorator
# Decorators allow to modify the behavior of functions or classes without directly changing the source code


def my_decorator(func):
    def inner():
        print("This is the decorator")
        func()

    return inner


@my_decorator
def outer_decorator():
    print("This is outer decorator")


outer_decorator()

# Example 4


def my_decorator(func):
    def wrapper(*args, **kwargs):
        # code to be executed before original function
        print("This is my decorator before function execution")
        result = func(*args, **kwargs)
        # code to execute after original function
        return result
        print("After function execution")

    return wrapper


@my_decorator
def my_function():
    print("Inside the function")


my_function()

# Example5


def my_decorator(cls):
    class ModifiedClass:
        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)

        def my_method(self):
            print("Modified method")

    return ModifiedClass


@my_decorator
class MyClass:
    def my_method(self):
        print("My original method")


my_instance = MyClass()
my_instance.my_method()

# Context Managers
# is an object that defines a temporary context for a block of code
# Example1: Demonstrate a context manager to open a file and returns a context manager instance


def open_file(filename):
    file = open(filename, "r")

    def __enter__():
        return file

    def __exit__(self, exc_type, exc_value, exc_tb):
        file.close()
        return __enter__, __exit__


with open_file("my_file.txt") as f:  # type: ignore
    contents = f.read()

# Example2: Demonstrate a context manager using a time series


import multiprocessing
import threading
import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        execution_time = end_time - self.start_time
        print(f"The time for this execution {execution_time} seconds elapsed")


# with example usage
with Timer():
    """measure execution time"""
    time.sleep(2)

# Multithreading and multiprocessing
# Techniques that can be used to improve the performance of a python program
# Multithreading is a technique where multiple threads are created within a single program
# Multiprocessing is a technique where multiple threads are created.

# Example3 of multithreading

import threading


def task(name):
    print(f"Running Task {name} ")


# Create multiple threads
threads = []
for i in range(10):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Example4 Demonstrate use of multiprocessing


def process(name):
    print(f"Processing task {name}")


# Create a pool of processes
pool = multiprocessing.Pool(processes=5)

# Submit multiple tasks to the pool
for i in range(6):
    pool.apply_async(process, args=(f"Process {i}",))

# Example5 Demonstrate use of multiprocessing and multithreading

import multiprocessing


def tasks(name):
    print(
        f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}"
    )


# create multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target=task, args=(f"Thread {i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# close the pool and wait until all processes finish
pool.close()
pool.join()

# Assignment A7:
# 1a) Show a context manager for file handling that automatically opens and closes a file.


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# Usage example
with FileManager("myfile.txt", "r") as file:
    data = file.read()
    print(data)

# b) Shows a context manager for managing a database connection.

import sqlite3


class DatabaseManager:
    def __init__(self, database):
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()


# Usage example
with DatabaseManager("example.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# c) Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.


def run_function(duration):
    print(f"Starting function for {duration} seconds...")
    time.sleep(duration)
    print("Function execution complete.")


# Multithreading example


def run_with_threads():
    durations = [1, 2, 3]  # Different durations for the function

    threads = []
    for duration in durations:
        thread = threading.Thread(target=run_function, args=(duration,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# Multiprocessing example

from multiprocessing import Process
import multiprocessing


def run_with_processes():
    durations = [1, 2, 3]  # Different durations for the function

    processes = []
    for duration in durations:
        process = multiprocessing.Process(target=run_function, args=(duration,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


# Running the examples
print("Multithreading example:")
run_with_threads()

print("\nMultiprocessing example:")
run_with_processes()

# Python for DataScience
"""
1. NumPy Functionalities: helps you work with arrays efficiently
2. Pandas - Functionalities: data cleaning, data transformation, merging, filtering
Data Visualization
Plotting - use a library called matplotlib or seabon - creates line, scatter, bar, histogram
and heatmaps

Key concepts in data science
1. Data(text, images, videos) or semi-structured(JSON, XML)
2. Data mining
3. Machine learning
4. Statistical analysis
5. Data Visualization
6. Big Data
7. Predictive analysis
"""

# Understanding data science workflow
"""
1. Problem definition
2. Data acquisition data.gov, kaggle, databases, external databases
Ensure data quality - data validation, cleaning, reprocessing

EDA - Data Exploratory Analysis
"""
# Data Preparation and preprocessing
"""
Missing data
Wrong format
Null values
"""
