print("\nOdd/Even Number Checker:")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
# -----------------------------------------------------------------------------------
print("\nNumber Guessing Game:")
import random

target = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == target:
        print("Correct! You guessed it.")
        break
    elif guess < target:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
        
# -----------------------------------------------------------------------------------
print("\nTriangle Pattern:")
rows = 5
for i in range(1, rows + 1):
    print("*" * i)  # Prints increasing number of stars
    
# -----------------------------------------------------------------------------------
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "/"))

# -----------------------------------------------------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  
# -----------------------------------------------------------------------------------

def count_word_freq(str):
    sentence = str if str else "apple banana apple cherry banana apple"
    words = sentence.split()

    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print(word_count)  
    
    
# -----------------------------------------------------------------------------------

def count_words_file(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        return len(words)

print("Word count:", count_words_file("example.txt"))

## _____________________________________________________________________
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.marks = []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average_marks(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0
 
s1 = Student("Alice", 20)
s1.add_mark(90)
s1.add_mark(85)

print(f"{s1.name}'s Average Marks: {s1.average_marks()}")  