#Advanced Object-Oriented Programming  

# 1: Inheritance

# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # <<---- super
        self.doors = doors

    def car_info(self):
        print(f"{self.brand} {self.model} has {self.doors} doors.")

# Creating an object of Car
car1 = Car("Toyota", "Corolla", 4)
car1.display_info()  # Inherited 
car1.car_info()      # Child 

# TODO - Extend


## _____________________________________________________________________

# 2: Method Overriding (Polymorphism)

class Animal:
    def speak(self):
        print("Animals make sounds")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")  

class Cat(Animal):
    def speak(self):
        print("Meow!")  

# Using overridden methods
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak()


## _____________________________________________________________________

# 3: Encapsulation (Data Hiding)
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number        # Public attribute
        self.__balance = balance                    # Private attribute (with double underscore)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}, New Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance  # Accessing private variable via method

# Creating an account
acc = BankAccount("12345", 5000)
acc.deposit(1000)
acc.withdraw(2000)

# Trying to access private variable (will cause an error)
# print(acc.__balance) 
print(acc.get_balance())  

## _____________________________________________________________________

#  https://medium.com/@prashampahadiya9228/abstract-classes-and-abstract-methods-in-python-e632ea34bc79#:~:text=In%20Python%2C%20abstract%20classes%20are,specifically%20the%20%60ABC%60%20class.&text=An%20abstract%20method%20is%20a,to%20implement%20these%20abstract%20methods.
# 4: Abstraction (Hiding Implementation Details)

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass  # Must be implemented in child classes

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

c = Circle(5)
r = Rectangle(4, 6)

print(f"Circle Area: {c.area()}")    
print(f"Rectangle Area: {r.area()}") 

## _____________________________________________________________________

# 5: Class vs. Instance Variables

class Employee:
    company = "TechCorp"  # Class variable (shared)

    def __init__(self, name, salary):
        self.name = name  # Instance variable (unique)
        self.salary = salary

e1 = Employee("Alice", 60000)
e2 = Employee("Bob", 70000)

print(e1.company) 
print(e2.company) 

Employee.company = "NewCorp"
print(e1.company)  

## _____________________________________________________________________

# 6: Static and Class Methods
'''
Static methods dont use self and behave like normal functions inside a class.
Class methods operate on the class itself rather than instances. 
'''
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        print(f"This class belongs to {cls.__name__}")

#  static method
print(MathOperations.add(5, 10))  

#  class method
MathOperations.info()  



## _____________________________________________________________________

# 6: Magic (Dunder) Methods

'''
Python has special methods with double underscores (__) that give objects special behavior
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):  
        return f"{self.title} by {self.author}"

    def __len__(self): 
        return 300

book = Book("Python 101", "John Doe")
print(book)       # <<--- print by default works on string 'str' 
print(len(book))  # Calls __len__ 
'''
Other dunder methods:
Method	    Purpose
__init__	Constructor (initialize attributes)
__str__	    String representation (print(obj))
__len__	    Defines behavior for len(obj)
__eq__	    Defines equality (==)
__add__	    Defines addition (obj1 + obj2)
'''

