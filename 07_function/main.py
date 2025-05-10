# def keyword is used to define a function 

def fun():
    print("Pakistan")

fun()
fun()
fun()
fun()

# parameters and arguments

def add(a,b):       # a and b are two parameters 
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print(add(5,10))     #5 and 10 are argumens 
print(sub(5,10))
print(mul(5,10))
print(div(5,10))

# Default Arguments


def defualtArgument(name, className="I am in 10th class"):
    print("My Name is", name)
    print(className)

defualtArgument("Javad")

# Recursion : a function call itself again and again
# suppose we want to find the factorial of n number using functions


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


takeInput = int(input("Enter your number: "))
print(factorial(takeInput))