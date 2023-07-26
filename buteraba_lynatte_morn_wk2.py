"""# Object Oriented Programming
# Key concepts in OOP are;
"""
"""1. class
2. object
3. encapsulation
4. polymorphism
5. abstractions
6. Inheritance"""
"""
# Class
# example1: Car
import math


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")


my_car = Car("Toyota", "Corona", 2007)
print(my_car.make)
print(my_car.model)
print(my_car.year)
print(my_car.start_engine())
print(my_car.stop_engine())


# example 3 : Rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return (self.length * self.width)

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    # Create a rectangle
rect = Rectangle(6, 8)
print(rect.length)
print(rect.width)
# calculate and display the area of the rectangle
print("Area:", rect.calculate_area())
# Calculate perimeter of the rectangle
print("Perimeter:", rect.calculate_perimeter())

# example 4: University student


class Student():
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print('Name:', self.name, 'Year:', self.year, 'Course:', self.course)


# create an instance of student
s1 = Student("Lynatte", 'BSc', 'Computer Science')
# call method
s1.display_details()

# Object
# An object is simply a collection of data fields and methods associated with it. For example, we
# can define our own class to represent cars as follows −


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is ", self.name)
        print("Iam ", self.age, "years old")


# create person object
p1 = Person("Gianna Tianna", 30)
p1.greet()

# Exercise: calculate area and circumference of a circle


class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_circumference(self):
        return (2*math.pi)*self.radius


c1 = Circle(5)
print(c1.radius)
print(c1.calculate_area())
print(c1.calculate_circumference())

# Exercise: calculate and display employee bonuses(15%) of salary (employee1 150000, employee2 230000)


class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        return self.salary*0.15


employee1 = Employee(1500000)
employee2 = Employee(230000)
print(employee1.calculate_bonus())
print(employee2.calculate_bonus())

# Encapsulation
# Key goals of encapsulation:
# data protection, info hiding, code organization and modularity, protect the object from changes
# example BankAccount


class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # deposit method
    def deposit(self, amount):
        self.balance += amount  # encapsulates the deposit

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return f"Balance is {self.balance}"


# create a bank object
my_account = Account("123456789", 1000)
# Access the Bank object and modify encapsulated attributes
print(f'My current Balance is ${my_account.get_balance()}')
print(my_account.account_number)
my_account.deposit(500)
print(my_account.balance)
my_account.withdraw(100)
print(my_account.balance)

# Exercise: Convert 37 degrees celsius to fahrenheit


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, celsius):
        self._celsius = celsius

    def get_fahrenheit(self):
        return ((self._celsius * 9/5)+32)

    def set_fahrenheit(self, fahrenheit):
        self._celsius = (fahrenheit-32)*5/9


celsius_value = 37
temperature_object = Temperature(celsius_value)
fahrenheit_value = temperature_object.get_fahrenheit()
print(f"{celsius_value} is equal to {fahrenheit_value} degrees Fahrenheit")


# Assignment2: show encapsulation with employee information to give pay increamentation
# salary with employee info to new_salary(850000 to 1000000)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_employee_info(self):
        return f"Name: {self.name}\nSalary: {self.salary}"

    def increase_salary(self, increment):
        self.salary += increment


# Creating an employee object
employee1 = Employee("Lynatte Buteraba", 850000)

# Getting employee information before incrementation
print("Employee Information (Before Incrementation):")
print(employee1.get_employee_info())

# Increasing salary by 150000
employee1.increase_salary(150000)

# Getting employee information after incrementation
print("Employee Information (After Incrementation):")
print(employee1.get_employee_info())"""

# Friday 30th June Morning session
# Inheritance
# Key Features of Inheritance in Python:
# 1. Enables classes to inherit attributes and behaviors from other classes.
# 2. Creates a hierarchy of classes, with base classes and derived classes.
# 3. Derived classes can access and use attributes and methods of the base class.
# 4. Allows overriding and extension of base class methods in the derived class.
# 5. Supports single, multiple, and multi-level inheritance.
# 6. Promotes code reusability and reduces code duplication.
# 7. Facilitates code organization, modularity, and extensibility.
# 8. Forms a hierarchical structure of related classes.
# 9. Provides flexibility in modeling real-world relationships and building complex systems.
# 10. Enables the creation of specialized classes based on existing ones.

# Examples
# Example Demonstrating Inheritance
# Parent class - Animal




from abc import ABC, abstractmethod
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


class Cat(Animal):
    def purr(self):
        print(f"{self.name} is purring.")


# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling methods of the base class
dog.eat()     # Output: Buddy is eating.
cat.sleep()   # Output: Whiskers is sleeping.

# Calling methods specific to the derived classes
dog.bark()    # Output: Buddy is barking.
cat.purr()    # Output: Whiskers is purring.


# Example 2
# class Vehicle:
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"The {self.color} {self.brand} starts.")

    def stop(self):
        print(f"The {self.color} {self.brand} stops.")


class Car(Vehicle):
    def __init__(self, brand, color, num_doors):
        super().__init__(brand, color)
        self.num_doors = num_doors

    def honk(self):
        print(f"The {self.color} {self.brand} with {self.num_doors} doors honks.")


class Motorcycle(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def wheelie(self):
        print(
            f"The {self.color} {self.brand} with {self.num_wheels} wheels performs a wheelie.")


# Creating instances of the derived classes
car = Car("Toyota", "Red", 4)
motorcycle = Motorcycle("Harley-Davidson", "Black", 2)

# Calling methods of the base class
car.start()        # Output: The Red Toyota starts.
motorcycle.stop()  # Output: The Black Harley-Davidson stops.

# Calling methods specific to the derived classes
car.honk()         # Output: The Red Toyota with 4 doors honks.
# Output: The Black Harley-Davidson with 2 wheels performs a wheelie.
motorcycle.wheelie()


# Exercise1: demonstrate using inheritance to calculate area and perimeter of a circle and rectangle


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating area and perimeter using the inherited methods
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

# Printing the results
print(f"Circle: Area = {circle_area:.2f}, Perimeter = {circle_perimeter:.2f}")
print(f"Rectangle: Area = {rectangle_area}, Perimeter = {rectangle_perimeter}")

# Multiple inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying")


class Bird(Animal, Flyable):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def display_info(self):
        super().display_info()
        print(f"Species: {self.species}")
        print(f"Name: {self.name}")


# create a bird object
my_bird = Bird("Pigeon", "bird")
# call functions on my_bird instance
my_bird.eat()
my_bird.fly()

# Method overriding


class Animal:
    def make_sound(self):
        print("Animal is making a sound")


class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")


class Cat(Animal):
    def make_sound(self):
        print("Cat is meowing")


def animal_make_sound(animal):
    animal.make_sound()


# Creating animal object
animal = Animal()
dog = Dog()
cat = Cat()
# calling make_animal_sound()
animal_make_sound(animal)
animal_make_sound(dog)
animal_make_sound(cat)

# Polymorphism
# Allows you to write code that can work with different objects
# Method overloading allows a class to have multiple methods with the same name but different parameters
# Example1


class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_circumference(self):
        return 3.14 * 2 * self.radius


rectangle = Rectangle(5, 5)
circle = Circle(5)
print("Rectangle Area: ", rectangle.calculate_area())
print("circle Area: ", circle.calculate_area())

# overloading


class Calculator:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z


calculator = Calculator()
print(calculator.add(3, 4))
print(calculator.add(2, 4, 6))

# Abstraction
# allows you to focus on essential features and hide them from unnecessary details
# Example: demonstrate abstraction


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car..")


class Truck(Vehicle):
    def start(self):
        print("Starting the truck..")

    def stop(self):
        print("Stopping the truck..")


car = Car()
truck = Truck()
car.start()
truck.start()
car.stop()
truck.stop()

# Exercise2: demonstrate abstraction using calculating area of a circle and rectangle


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius**2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# Creating instances of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Calculating area and perimeter using the abstract methods
circle_area = circle.calculate_area()
circle_perimeter = circle.calculate_perimeter()

rectangle_area = rectangle.calculate_area()
rectangle_perimeter = rectangle.calculate_perimeter()

# Printing the results
print(circle.calculate_area())
print(rectangle.calculate_area())
print(circle.calculate_perimeter())
print(rectangle.calculate_perimeter())

# Assignment create a receipt printing program with GUI


class ReceiptApp:
    def __init__(self, master):
        self.master = master
        master.title("Receipt Printing Program")

        # Create labels, entry fields, and buttons
        self.label_item = tk.Label(master, text="Item:")
        self.label_item.grid(row=0, column=0, sticky="E")
        self.entry_item = tk.Entry(master)
        self.entry_item.grid(row=0, column=1)

        self.label_price = tk.Label(master, text="Price:")
        self.label_price.grid(row=1, column=0, sticky="E")
        self.entry_price = tk.Entry(master)
        self.entry_price.grid(row=1, column=1)

        self.button_add = tk.Button(
            master, text="Add Item", command=self.add_item)
        self.button_add.grid(row=2, columnspan=2)

        self.receipt_text = tk.Text(master)
        self.receipt_text.grid(row=3, columnspan=2)

        self.button_print = tk.Button(
            master, text="Print Receipt", command=self.print_receipt)
        self.button_print.grid(row=4, columnspan=2)

        self.button_remove = tk.Button(
            master, text="Remove Item", command=self.remove_item)
        self.button_remove.grid(row=5, columnspan=2)

        self.receipt_items = []

    def add_item(self):
        item = self.entry_item.get()
        price = self.entry_price.get()

        if item and price:
            self.receipt_items.append((item, price))
            self.entry_item.delete(0, tk.END)
            self.entry_price.delete(0, tk.END)
            self.display_items()

    def remove_item(self):
        selected_indices = self.receipt_text.curselection()
        if selected_indices:
            selected_index = int(selected_indices[0])
            del self.receipt_items[selected_index]
            self.display_items()

    def display_items(self):
        self.receipt_text.delete(1.0, tk.END)
        for item, price in self.receipt_items:
            self.receipt_text.insert(tk.END, f"{item} - UGX{price}\n")

    def print_receipt(self):
        receipt_content = ""
        total_amount = 0

        for item, price in self.receipt_items:
            receipt_content += f"{item} - UGX{price}\n"
            total_amount += float(price)

        if len(self.receipt_items) > 5:
            discount = total_amount * 0.2
            total_amount -= discount
            receipt_content += f"\nDiscount (20%): ${discount:.2f}"

        receipt_content += f"\nTotal Amount: UGX{total_amount:.2f}"

        # You can add code here to perform actual receipt printing

        print(receipt_content)

        # Clear the receipt after printing
        self.receipt_items = []
        self.display_items()


# Create the Tkinter window
root = tk.Tk()
app = ReceiptApp(root)
root.mainloop()
