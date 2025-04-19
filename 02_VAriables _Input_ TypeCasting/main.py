a = 10
b = 20

b += 5

print(a + b)

c = a > b  # false
c = a < b  # true

d = a == b  # false

print(c)
print(d)

# TruthTable

e = True or False

print(e)


# TruthTable of or
print("True or False is", True or False)  # True
print("True or True is", True or True)  # True
print("False or Turn is", False or True)  # True
print("False or False is", False or False)  # False

# TruthTable of and
print("True and False is", True and False)  # False
print("True and True is", True and True)  # True
print("False and Turn is", False and True)  # False
print("False and False is", False and False)  # False


print(not (True))  # False
print(not (False))  # True


# How to find the type of a variable

a = 20

print(type(a))

a = "20"

print(type(a))

# How to convert a variable from one type to another

a = 20

typeConvert = str(a)  # ---> to string
typeConvert = float(a)  # ---> to float
typeConvert = bool(a)  # ---> to True
typeConvert = int(a)  # ---> to integer
typeConvert = not (bool(a))  # ---> to False


t = type(typeConvert)

print(t)

print(typeConvert)


# How to take input from the user

a = int(input("Enter your 1 number : "))
b = int(input("Enter your 2nd number : "))

if type(a) == str:
    print("You have entered a string")
    print(type(a))
else:
    print("Your 1st number is", a)
    print("Your 2nd number is", b)
    print(a + b)

# Making Simple Calculator With Error Handling

a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
operation = input("Enter the operation you want to perform : ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Invalid operation")

# For example, if we want to add two numbers, we need to convert them to integers before performing the addition


# Problem 1 (Finding Remainder)

a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))

c = a / b  #  this will give the decimal part
c = a // b  #  this will remove the decimal part
print(c)
c = a % b
print(c)


# Problem 2 (Finding the average of 3 numbers)

a = int(input("Enter your 1st number : "))
b = int(input("Enter your 2nd number : "))
c = int(input("Enter your 3rd number : "))
e = int(input("Enter your 4th number : "))
f = int(input("Enter your 5th number : "))

average = (a + b + c + e + f) // 5

print("The average of the 5 numbers is", average)


# Problem 3 (Finding Square of the number)

a = int(input("Enter the number : "))

sqaureRoot = a**2

print("The squareRoot of the number is", sqaureRoot)


# String

a = "Hello Python"

# finding the length of the string
print(len(a))