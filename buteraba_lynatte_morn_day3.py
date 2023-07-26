#Basic operators and Expressions(Input and Output) 
# Arithmetic operators
"""
- Addition(+): Adds 2 operands together.add()
- Subtraction(-): Subtracts the second operand from the first.
- Multiplication(*): Multiplies two operands
- Division(/): Divides the first operand by the second
- Modulo(%): Returns the reminder of the division
- Exponentiation(**): Raises the first operand to the power of the second.
- Floor Division(//): Returns the quotient of the division, discarding the remainder.
"""
#2 Assignment operators
"""
- Assign(=): Assigns a value to a variable.
-Add and assign(+=): Adds the right operand and assigns the result to the left operand.
- Subtract and assign(-=): Subtracts the right operand from the left operand and assigns the result to the left operand.
- Multiply and assign(*=): Multiplies the right operand with the left operand and assigns the result to the left operand.
- Divide and assign(/=): Divides the left operand by the right operand and assigns the result to the left operand.
- Modulo and assign(%=): Computes the modulus of the left operand with the right operand and assigns the result to the left operand.
- Exponentiate and assign(**=): Raises the left operand to the power of the right operand and assigns the result to the left operand.
- Floor Divide and assign(//=): Performs floor division on the left operand by the right operand and assigns the result to the left operand.

"""
#3 Comparison operators
"""
- Equal to(==): Checks if two operands are equal.
- Not equal to(!=): Checks if two operands are not equal.
-  Greater than(>): Checks if the left operand is greater than the right operand.
- Less than(<): Checks if the left operand is less than the right operand.
- Greater than or equal to(>=): Checks if the left operand is greater than or equal to the right operand.
- Less than or equal to(<=): Checks if the left operand is less than or equal to the right operand.
"""
#4 Logical operators
"""
- Logical AND(and): Reaturns True if both operands are true.
- Logical OR(or): Returns True if at least one of the operands is true
- Logical NOT(not): Returns the opposite of the operands's truth value.
"""
# Membership operators
"""
- In: Returns True if a value if found in a sequence.
- Not in: returns True if a value is not found in a sequence.
"""
# 7 Identity operators
"""
- is: returns True if both operands refer to the same object.
- is not: returns True if both operands dont refer to the same object.
"""
# Examples of comparison operators
# comparison operators
a = 15
b = 9
# Greater than
if a > b:
    print('a is greater than b')
    print(a>b)

#Less than 
if a < b:
    print('a is less than b')
    print(a<b) 

#Greater than or equal to
if a >= b:
    print('a is greater than or equal to b')
    print(a>=b)

#Less than or equal
if a <= b:
    print('a is less than or equal to b')
    print(a<=b) 

#Equal to
if a == b:
    print('a is equal to b')
    print(a==b) 

#Not equal
if a != b:
    print('a is not equal to b')
    print(a!=b) 

#Less than or equal to
print(a<=b)

#Equal to
print(a==b)              
       
#Logical operators examples
a = True
b = False

#Logical AND
print(a and b)

#Logical OR
print(a or b)

#Logical NOT
print(not a)
print(not b)

#Assignment operators
#compound assignment operators
a = 5
# add and assign
a += 5
print(a)

# subtract and assign
a = 19
a -=5
print(a)

# multiply and assign
b = 32
b *=2
print(b)

# divide and assign
c = 10
c /=4
print(c)

# modulus and assign
d = 20
d %=6
print(d)

# exponential and assign
f = 2
f **=4
print(f)

# membership assignment operators
cars = ['Jeep', 'Tesla', 'BMW', 'RollsRoyce']
if 'Jeep' in cars:
    print('Jeep is in the list')
    print("Tesla"  in cars)
    print('Toyota' in cars)
    
# Identity operators
x = 10
y = 10
# is operator 
print(x is y)
print(x is not y) 
print(x == y)
print(x != y)
print(x < y)
print(x <= y) 

# List
z = [1,2,3,4,5,6,7]
w = [1,2,3,4,5,6,7] 
print(z is not w)

# 8 Bitwise operators
# Bits of binary numbers

"""Bitwise operators are used to perform operations on individual bits of binary numbers.
Bitwise AND(&) : Performs a bitwise AND operation between the corresponding bits of 2 numbers
Bitwise OR('|') : Performs a bitwise OR operation between the corresponding bits of 2 integers
Bitwise XOR('^') : performs a bitwise XOR operation 
Bitwise NOT('~') : performs a bitwise NOT operation between the corresponding bits of 2 integers
Bitwise left shift('<<') : performs a bitwise left shift operation
Bitwise right shift('>>') : performs a bitwise right shift operation 
""""
# Examples of bitwise operations
a = 10 # 1010 in binary
b = 20
# Bitwise AND operation
result_and = a & b
print(result_and)

#Bitwise OR
result_or = a | b
print(result_or)

#Bitwise XOR
result_xor = a ^ b
print(result_xor)

#Bitwise NOT
result_not = a ~ b
print(result_not)

#Bitwise leftshift
result_left_shift = a << b
print(result_left_shift)

#Bitwise right shift
result_right_shift = a >> b
print(result_right_shift)

# Create a simple calculator function to calculate(add, subtract, multiply, divide)
def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print('Lynatte Simple Calculator')
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter the operator '+, -, *, /):")
    
    if operator =='+':
        result = add(number1, number2)
    elif operator == '-':
        result = subtract(number1, number2)    
    elif operator == '*':
        result = multiply(number1, number2)  
    elif operator == '/':
        result = divide(number1, number2) 
    else:
        print('Invalid operator')   
        return 
    print("The result is: ", result) 
if __name__ == '__main__'  :
        main()
    # print("Addition: ", add(a, b))           
    # print("Subtraction: ", subtract(a, b)) 
    # print("Multiplication: ", multiply(a, b)) 
    # print("Division: ", divide(a, b)) 

#tkinter learn
# Assignment1 create a simple calculator program with a GUI interface. 
#Make the title of the calculator program window with your name 
import tkinter as tk # for creating the GUI interface.

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Lynatte Simple Calculator")

# Create the display entry widget
display = tk.Entry(window, width=30, justify=tk.RIGHT, font=('Arial', 12))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create the number buttons
button_1 = tk.Button(window, text="1", padx=10, pady=5, command=lambda: button_click(1))
button_2 = tk.Button(window, text="2", padx=10, pady=5, command=lambda: button_click(2))
button_3 = tk.Button(window, text="3", padx=10, pady=5, command=lambda: button_click(3))
button_4 = tk.Button(window, text="4", padx=10, pady=5, command=lambda: button_click(4))
button_5 = tk.Button(window, text="5", padx=10, pady=5, command=lambda: button_click(5))
button_6 = tk.Button(window, text="6", padx=10, pady=5, command=lambda: button_click(6))
button_7 = tk.Button(window, text="7", padx=10, pady=5, command=lambda: button_click(7))
button_8 = tk.Button(window, text="8", padx=10, pady=5, command=lambda: button_click(8))
button_9 = tk.Button(window, text="9", padx=10, pady=5, command=lambda: button_click(9))
button_0 = tk.Button(window, text="0", padx=10, pady=5, command=lambda: button_click(0))

# Create the operator buttons
button_add = tk.Button(window, text="+", padx=10, pady=5, command=lambda: button_click("+"))
button_subtract = tk.Button(window, text="-", padx=10, pady=5, command=lambda: button_click("-"))
button_multiply = tk.Button(window, text="*", padx=10, pady=5, command=lambda: button_click("*"))
button_divide = tk.Button(window, text="/", padx=10, pady=5, command=lambda: button_click("/"))
button_clear = tk.Button(window, text="C", padx=10, pady=5, command=button_clear)
button_equal = tk.Button(window, text="=", padx=10, pady=5, command=button_equal)

# Position the buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)

# Start the main loop
window.mainloop()
    
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          