#Execute Python Syntax
print("Hello World!!")

#Python Indentation
if 5 > 2:
    print("Five is greater than two")

#Python Variables
x = 5
y = 2
z = "Hello World!!"

if x > y:
    print("Five is greater than two")

#Comments
#This is a comment!!
print("International Day to End obstetric Fistula")

#You can use comments to prevent the execution of codes.
#print("Hello World!!")

#Multiline Comments
#You
#Can
#Either
#Do
#This
     #OR
"""
This😉
"""
print("Glory to the Lord")

#Python Variables
a = 4
b = "Jesse"
print(a)
print(b)

#output will be the string and not the int
c = 6
c = "Sally"
print(c)

#Casting:Specifying the data type of variable
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Get the type
x = 5
y = "Jesse"
print(type(x))
print(type(y))

#Single or Double Quotes
x = "Jesse"
#is the same as
x = 'Jesse'

#Case-Sensitive
r = 4
R = "Jesse"
#A will not overwrite a

#Python-Variable Names
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#All these are different variables
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Multi Words Variable Names
#Camel Case:Each word, except the first,starts with a capital letter
myVariableName = "John"

#Pascal Case:Each Word starts with a capital letter
MyVariableName = "John"

#Snake Case:Each word is separated by an underscore
my_variable_name = "John"

#Assign Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Assign one value to Multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple", "Banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables
x = "Python is awesome"
print (x)

x = "Python"
y = "is"
z = "awesome"
print(x, y,z)

       #ORR
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Notice the space after python and is, if they weren't there it would print "Pythonisawesome"

#For numbers
x = 5
y = 7
print(x + y)

"""
Python gives an error when you use the print function 'print()' to try and combine a string and a number with the + operator
Output using ","
"""
x = 5
y = "Jesse"
print(x, y)

#Global Variables:Variables created outside a function

x = "awesome"

def myfunc():
    print("Python is",x)

myfunc()

#ORRRR
x = "awesome"

def myfunc():
    print("Python is "+ x)

myfunc()

#Note, when using '+', use space, otherwise, it'll space itself

"""
If you create a variable with the same name inside a function,
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was, global and with the 
original value.
"""

x = ("awesome")

def myfunc():
    x = ("Fantasic")
    print("Python is " + x)
myfunc()

print("Python is " + x)

#Global keyword:Used to create a global variable inside a function

def myfunc():
    global x
    x = "Amazing"
myfunc()

print("Python is " + x)

#You can also use global keyword to change a global variable inside a function
x = "awesome"

def myfunc():
    global x
    x = "FANTASTIC"
myfunc()

print("Python is " + x)







