with open("sample.txt", "w") as f:
    f.write("Hello, file!")

"""
Mode	Description
'r'	    Read mode (default)
'w'	    Write mode (overwrites the file)
'a'	    Append mode (adds to the file)
'x'	    Create mode (fails if file exists)
'b'	    Binary mode (e.g., 'rb', 'wb')
"""

# Opening a File
file = open("example.txt", "r") 


# Reading a File
# Read the entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # Returns a list of lines


# Writinmg to a file
# Writing to a file (overwrites existing content)
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending a new line!\n")
