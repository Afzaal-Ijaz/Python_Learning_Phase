# This is the decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

    # This is the function that will be decorated
@my_decorator
def sum():
    print('I am a sum..')

    
sum()