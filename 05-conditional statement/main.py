
year = int(inut("Enter a year here"))    # get input from user

if year%2 == 0:
    print("this is a leap year")        #if reminder is equal to zero means it is a leap year 

else:
    print("This is not a leap year")


print(" program end")
 
age = int(input("Enter your age: "))                       # get input from user

if age >= 18:
    print("You are an adult you can make your CNIC")       #if greater than 18 means eligibale

elif age <= 0:
    print("please enter a valid age")                     #if input is invalid 

elif age < 12:
    print("You are a child you can't make your CNIC")     #you are to young 


print(" program end")


