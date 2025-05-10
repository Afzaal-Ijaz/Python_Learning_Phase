class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def walk(self):
        print('He is Walking...')

class Student(Person):
    roll_no = 1231
    def register_course(self):
        print('Computer Science course is registered')

student1 = Student('Afzaal', 20, 'male')
student1.name                            #parent class attribute
student1.walk()                           #parent class method
student1.register_course()                 #child class method