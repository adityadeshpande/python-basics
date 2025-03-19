class Person:
    def __init__(self, name):
        self.name = name
p = Person("Bob")
print(p.name)



# Defining a class
class Car:
    pass  # Empty class

# Creating an object (instance) of Car
my_car = Car()
print(type(my_car)) 





class Car:
    # Class attribute (shared by all objects)
    wheels = 4  

    def __init__(self, brand, model, year):
        self.brand = brand  # Instance attribute
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 1997)
car2 = Car("Honda", "Civic", 2001)

car1.display_info()  
car2.display_info()  

print(car1.wheels)   
print(car2.wheels)   



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
person1 = Person("Bob", 30)
person1.greet()  


# --------------------------------------------------------------------

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")

mustang = Car("Ford", "Mustang", 2022, "Red")
bmw = Car("BMW", "m3", 2023, "Black")

mustang.start()  
bmw.stop()  ## ToDo- Make this logical 
mustang.start() ## ToDo- Make this logical 
