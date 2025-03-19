def add(a, b):
    return a + b
print(add(3, 5))



def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")

introduce("Bob")  
introduce(age=25, name="Charlie")  



def variableList(name, *lst):
    print(f"{name}:{lst}")
    for x in lst:
        print(x)

variableList("Bob", 1,2,3,4,5)
# discuss *lst