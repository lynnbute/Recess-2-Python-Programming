#Object Oriented Programming
#Key concepts in OOP are;
"""
1. class
2. object
3. encapsulation 
4. polymorphism
5. abstractions
6. Inheritance
"""
# Class
# example1: Car
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
        return 2* (self.length + self.width)
    # Create a rectangle
rect = Rectangle(6,8)
print(rect.length)
print(rect.width)
# calculate and display the area of the rectangle
print ("Area:", rect.calculate_area())
# Calculate perimeter of the rectangle
print ("Perimeter:", rect.calculate_perimeter())
    
# example 4: University student
class Student():
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course
        
    def display_details(self):
        print('Name:', self.name,'Year:', self.year,'Course:', self.course)
        
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
p1=Person("Gianna Tianna",30)
p1.greet()

# Exercise: calculate area and circumference of a circle
import math
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
#Key goals of encapsulation: 
# data protection, info hiding, code organization and modularity, protect the object from changes
# example BankAccount
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    # deposit method 
    def deposit(self, amount):
        self.balance += amount # encapsulates the deposit
        
    def withdraw(self, amount):
        if self.balance >=amount :
            self.balance -= amount 
        else: 
            print("Insufficient funds")
            
    def get_balance(self):
        return f"Balance is {self.balance}"
    
# create a bank object
my_account =Account("123456789", 1000) 
#Access the Bank object and modify encapsulated attributes
print (f'My current Balance is ${my_account.get_balance()}')
print(my_account.account_number)
my_account.deposit(500)
print(my_account.balance)
my_account.withdraw(100)
print(my_account.balance)
    
# Exercise: Convert 37 degrees celsius to fahrenheit
class Temperature:
    def __init__(self, celsius):
        self._celsius= celsius
        
    def get_celsius(self):
        return self._celsius
    
    def set_celsius(self, celsius):
        self._celsius=celsius
        
    def get_fahrenheit(self):
        return ((self._celsius * 9/5)+32)
    
    def set_fahrenheit(self, fahrenheit):
        self._celsius=(fahrenheit-32)*5/9
        
celsius_value = 37
temperature_object =Temperature(celsius_value)
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
print("\nEmployee Information (After Incrementation):")
print(employee1.get_employee_info())

    
    
        
    

    
            
        
          