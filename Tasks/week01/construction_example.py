'''
Use class-level attributes (root of the class) on for values that are  the same for every object.

Examples:
- Number of wheels on a car
- Pi constant
- Configuration shared by all instances
- Versions numbers...
'''

class Car:
    wheels = 4 # same for all cars aas a default.

'''
These attributes live on the class, not the object

Use constructor (__init__) for instance-specific data. They are unique per object.

Examples:
- Car color
- Max speed
- Current speed
- Registration number
'''

class Car:
    wheels = 4 # Shared by default by all cars

    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

'''
Every time you create a new object, contructor (__init__) runs and gives that specific object its own attributes.

Why not put object-specific attributes in the root? Because attributes in the root are shared unless overwritten.

For example:
'''        

class Person:
    hobbies = [] # shared list

p1 = Person()
p2 = Person()

p1.hobbies.append("Football")
p1.hobbies.append("Reading")
p2.hobbies.append("Making music")

print(p2.hobbies)

'''
If the list was inside __init__, each would get its own list.
'''

class Student:
    hobbies: list

    def __init__(self):
        self.hobbies = []

s1 = Student()
s2 = Student()

s1.hobbies.append("Football")
s1.hobbies.append("Reading")
s2.hobbies.append("Gym")


print(s1.hobbies)
print(s2.hobbies)