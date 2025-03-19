text = "hello world"
print(text.upper(), text.replace("hello", "hi"))

# String Operations and Methods

# Length:
text = "Hello, World!"
print(len(text))  
 
# Replace
sentence = "I love Python!"
new_sentence = sentence.replace("love", "enjoy")
print(new_sentence)   

# Split
data = "apple,banana,grape,orange"
fruits = data.split(",")  
print(fruits)  

words = "Hello World".split()
print(words)  

# Join
fruits = ['apple', 'banana', 'grape']
result = ", ".join(fruits)
print(result)  


# String Formatting
# Using f-strings (Recommended)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

#Using .format() Method
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))

#Using Pos Placeholdrs
print("Hello {1}, meet {0}.".format("Alice", "Bob"))
print("Name: {name}, Age: {age}".format(name="Alice", age=22))
