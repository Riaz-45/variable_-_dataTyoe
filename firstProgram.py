print("Hello World!")
#this is my first line in python code
"""                              
name = 'Riaz'
age = 26
price = 25.99
print(name,age,price)
print("My name is : ", name)
print("My age is : ", age)

age2 = age
print(age2)
print(type(name))
print(type(age))
print(type(price))

age = 23
old = False
a = None
print(type (old))
print(type (age))
print(type (a))

"""


#relational operators
"""
x = 5
y = 8
print(x == y) #False
print(x != y) #True
print(x >= y) #False
print(x <= y) #True

"""


#logical operators

"""
a = 50
b = 30
print(not False)
print(not (a > b))

print("ans of the AND operator: ", (a > b) and (a != b) ) #true
print("ans of the OR operator: ", (a > b) or (a == b) ) #true

val1 = True
val2 = False
print("ans of the AND operator: ", val1 and val2 ) #false
print("ans of the OR operator: ", val1 or val2 ) #true

"""


#Type Conversion

"""
a = 2 #int
b = 4.25 #float
sum = a + b # 2.0 + 4.25 = 6.25 (automatic "a" float e convert hoye jabe because float is superior to integer)
print(sum) #float

x = "2" #string
y = 6.25 #float
# print(x + y) #typeError happen;
print(int(x) + y) #typecasting

"""


#Input in Python

"""

name = input("enter your name: ")
print("welcome", name)

#*Input function e kono value input korle seta sobsomoy "String" value hisebe input nibe*

#*tie individual value input dite hole Inout function er age oi value er type ta mention kore dite hobe like...{int(input("Enter Name:"))}*

val = int(input("Enter some value: "))
val = float(input("Enter some value: "))
print(type(val), val)

name = input("enter name: ")
age = int(input("enter age: "))
marks = float(input("enter marks: "))

print("welcome", name)
print("age", age)
print("marks", marks)

"""

#Area of a square

a = float(input("enter the length: "))
print("Area is: ", a ** 2)

#problem solving

a = int(input("enter a: "))
b = int(input("enter b: "))
print(a >= b)