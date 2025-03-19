try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")



try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


try:
    lst = [1, 2, 3]
    print(lst[5])  # IndexError
except Exception as e:
    print(f"An error occurred: {e}")



try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")



try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")  # runsonly if no error


# ---------------------------------------------------------------------



while True:
    try:
        age = int(input("Enter your age: "))
        if age <= 0:
            raise ValueError("Age must be positive!")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

print(f"Your age is {age}.")
