# Class Notes

# Introduction
- 2:15
Small projects on 2nd semester
big project later (Topic: EV)

### Notes
- Explain as much as you can
- Organize repository well (named structure)
- In the end of the class. small practice project with Rakkaranta.
- All tasks are uploaded in GitHub.
- Test is about the project
- Grade mainly from test results with all task submitted.
- 2 skips max for this semester. 0.5 credit reduction per class after (or doctor's certificate).
- Study groups (ex. discuss the tasks from last week.)
- Only return code which you understand.
- Practice presentation. KNOW YOUR CODE.

```__count: int```
It keeps the function private. So that it can't be accessed outside of the class/function

### Deserializing
Reading data --> object
### Serializing
object --> data
(csv)

### Notes about meeting
if there isn't a need for a meeting do not hold a meeting.\
But if a team member needs help with the homework.

### General notes
- Do docstrings for you methods / functions
- Header comments

### What is an abstract method?
Family (common attribute)
- culture
- hair color
- holidays
- hobbies

### "private" functions
- single underscore = naming convention
- double underscore = private

## Pillars
1. Inheritance
    Super class ---(Properties  Methods)--> Subclass class --> Object
    - Purpose: **reuse** existing code
    - Reusuable class is **generic**
    - By inheriting some class, the subclass gets:
        - Properties and methods from the super class the are "public" or "protected"

    ### Example
    #### **No inheritance**
    ```
    class Cat():
        sound: str
        def __init__(self) -> None:
            self.sound = "Meow!"
            return None
        def makeSound(self) -> None:
            print(self.sound)
            return None

        class Dog():
            sound: str
            def __init__(self) -> None:
                self.sound = "Woff!"
                return None

            def makeSound(self) -> None:
                print(self.sound)
                return None
    ```
    #### **Inheritance** (Inheriting Animal)
    ```
    class Animal:
        sound: str
        def __init__(self, sound: str) -> None:
            self.sound = sound
            return None
        def makeSound(self) -> None:
            print(self.sound)
            return None

    class Cat(Animal):
        def __init__(self) -> None:
            super().__init__("Meow!")
            return None

    class Dog(Animal):
        def __init__(self) -> None:
            super().__init__("Wuff!")
            return None
    ```


2. Abstraction
    **Making abstraction of an animal**
    Draw an animal.
    Don't draw any specific animal.

    Draw a vehicle.
    Don't draw any specific vehicle.

    ### **Abstact Classes**
    - Template for building other class
        - (Abstract Base Class)
    - Example
        - **Animal** is **abstact class**
        - **Cat** is **concrete class**

    <!-- - Abstract class can have methods with implementations in them
        - Difference to interfaces here is that interfaces can't have implementations 
    - Defining abstract class means that developer may not create instance directly from it -->

3. Polymorphism 
4. Encapsulation

### Development example - Car
- Program needs "Car" objects with following aspects:
- Properties:
    - Position
    - seats
    - EngineOn status
- Methods:
    - Way to accelerate
    - Way to steer

### Development example motorcycle
- The next development stage requires adding "Motorcycle" objects
- Properties:
    - Position
    - Seats
    - EngineOn status
- Methods:
    - Way to accelerate
    - Way to steer

### Similarities
- Both "Car" and "Motorcycle" have similarities
- Still, they have their differences
- There are cases where **reusing** existing classes will be handy...