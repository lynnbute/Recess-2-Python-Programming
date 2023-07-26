# Python conditions and if statements
#An "if statement" is written by using the if keyword.
#if condition1:
    # code block executed if condition1 is true
#elif condition2:
    # code block executed if condition2 is true and condition1 is false
#else:
    # code block executed if both condition1 and condition2 are false

a=20
if a%2 == 0:

    print("a is an even number")

# if else statement
#if the condition is false, the else block code is executed. 
a=20
if a%2 == 0:

    print("a is an even number")
else:
    print("a is an odd number")

# nested ifs
#this is when an if statement is inside another if statement
    # Assume a student's grade
grade = 85

# Check the grade using nested if statements
if grade >= 90:
    print("Grade: A")
    if grade >= 95:
        print("Excellent!")
elif grade >= 80:
    print("Grade: B")
    if grade >= 85:
        print("Good job!")
else:
    print("Grade: C")
    if grade >= 70:
        print("You can do better!")

print("End of program")

# Examples
age = 20
if age < 18:
    print('You are underage')
elif age >= 18 and age <= 65:
    print('you are an adult') 

number =2023   
if number % 2 == 0:
    print("Even number") 
elif number % 2 != 0:
    print("Odd number")
else:
    print("Invalid number")
          
     

#Loops
# for loop:
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
# It executes a block of code for each element in the sequence.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  # while loop:
# The while loop is used to repeatedly execute a block of code as long as a certain condition is true.
# It keeps executing the code block until the condition becomes false.
i = 1
while i < 6:
  print(i)
  i += 1
# Break and continue statements
# Break jumps out of a loop when a condition is reached 
for number in range(1, 10):
    if number == 5:
        break
    print(number)
        
# continue statement
for number in range(1, 10):
    if number == 5:
        continue
    print(number)  

# Exception handling(try, except, finally)
# except is used to handle specific type of exceptions when they occur.
#try:
    # code that may raise an exception
    # It allows you to catch and handle specific exceptions gracefully, preventing the program from crashing.
#except SomeException:
    # code executed if SomeException is raised
#except AnotherException:
    # code executed if AnotherException is raised
#else:
    # code executed if no exceptions are raised
#finally:
    # code executed regardless of whether an exception occurred or not
#try:
     #x = int(input("Enter a number: "))
# Example
emotion = {
    'happy' : "I am happy you're here"
    'sad' : "I amm sorry to hear that you're feeling sad"
    'angry' : "If you're angry take a deep breath"
    'fearful' : 'I understand that fear can be challenging'
    'disgusted' : 'I easily get disgusted, sorry'
}
# prompt users to put their feelings
user_input = input("How are you feeling?")  
emote = emote.lower() 
# List of fruits(example of try-except, finally)
fruits = ["Mango", "Apple", "Grapes", "Berries"]

try:
    
    index = int(input("Enter the index of the fruit you want to access: "))


    selected_fruit = fruits[index]
    print("Selected fruit:", selected_fruit)

except IndexError:
    print("Invalid index! The list does not have an element at the specified index.")

except ValueError:
    print("Invalid input! Please enter a valid integer index.")

except Exception as error:
    print("An error occurred:", str(error))

finally:
    print("Exception handling completed.")

  
# Exercise: write a program to ask students about their mental health, prompt students on a scale of 1 to 10 to rate their mental health
        # Initialize an empty list to store the responses
responses = []

# Prompt for student information until the user decides to stop
while True:
    name = input("Please enter your name (or 'q' to quit): ")
    if name.lower() == 'q':
        break
    rating = int(input("On a scale of 1 to 10, how would you rate your mental health? "))
    response = input("How are you feeling today? ")

    # Store the response in a dictionary
    student_info = {"name": name, "rating": rating, "response": response}
    responses.append(student_info)

# Print the collected responses
print("\nCollected Responses:")
for student in responses:
    print(f"Student: {student['name']}")
    print(f"Rating: {student['rating']}")
    print(f"Response: {student['response']}")
    print()
