# works when one wants to combine a string to a number
#we need to use format() method
#this format() takes the passed parameters, formats them and places them in the string where the placeholders{} are
age = 23
#name = "My name is Kim, i am " + age
name = "My name is jun and i am {}"

print(name.format(age))