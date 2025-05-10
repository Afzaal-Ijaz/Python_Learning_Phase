class Person():
    def __init__(self, name, age): # constructor method
        self.name = name # object attriburtes
        self.age = age # object attriburtes
    
    def walk(self): # object methods
        print('The person is walking')

p1 = Person('Arslan', 30)
p2 = Person('Afzaal', 20)
print(p1.name)
print(p2.name)

p2.walk()