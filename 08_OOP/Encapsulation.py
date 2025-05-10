
# Encapsulation in oop


class Info:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.gender = gender

    def get_full_info(self):
        return f"Student  name is {self.__name + ", age is " + self.__age} and gender is {self.gender}."


data = Info("Ali", "20", "male")
# print(
#     data.__name
# ) --------------> it will give error because we have used __ before the variable name which made the variable private
print(data.gender)
print(data.get_full_info())

# in short we use encapsulation to make variable private once we make any variable private it cant not be accessable outside the class, but we can use the private variable in the class in which the variable is declared
