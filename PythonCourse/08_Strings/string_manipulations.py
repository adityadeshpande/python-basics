# String Manipulation

# Count Vowels in a String
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(count_vowels("Hello World"))  


# Reverse a String Without Using [::-1]
def reverse_string(text):
    return "".join(reversed(text))

print(reverse_string("Python"))  

# Check if a String is a Palindrome
def is_palindrome(text):
    text = text.lower().replace(" ", "")  
    return text == text[::-1]

print(is_palindrome("madam"))    
print(is_palindrome("hello"))   
print(is_palindrome("race car")) 


# Capitalize Each Word in a Sentence.

sentence = "hello world, welcome to python!"
capitalized = sentence.title()
print(capitalized) 


## OUT OF SCOPE BUY WHY NOT!!
from collections import Counter

def most_frequent_char(text):
    return Counter(text.replace(" ", "")).most_common(1)[0]

print(most_frequent_char("banana"))  




"""
Python String Methods
Python provides various built-in methods to manipulate and process strings.

1. Basic String Methods
   - len(s)        : Returns the length of the string.          -> len("Hello") → 5
   - str(obj)      : Converts an object into a string.          -> str(100) → "100"

2. Case Manipulation Methods
   - s.lower()     : Converts all characters to lowercase.      -> "HELLO".lower() → "hello"
   - s.upper()     : Converts all characters to uppercase.      -> "hello".upper() → "HELLO"
   - s.capitalize(): Capitalizes the first letter.              -> "python".capitalize() → "Python"
   - s.title()     : Capitalizes the first letter of each word. -> "hello world".title() → "Hello World"
   - s.swapcase()  : Swaps uppercase to lowercase and vice versa. -> "PyThOn".swapcase() → "pYtHoN"

3. String Searching Methods
   - s.find(sub)   : Returns the first occurrence index of sub or -1 if not found.  -> "hello".find("l") → 2
   - s.rfind(sub)  : Returns the last occurrence index of sub.                      -> "hello".rfind("l") → 3
   - s.index(sub)  : Like find(), but raises an error if not found.                 -> "hello".index("l") → 2
   - s.rindex(sub) : Like rfind(), but raises an error if not found.                -> "hello".rindex("l") → 3
   - s.count(sub)  : Returns the number of occurrences of sub.                      -> "banana".count("a") → 3

4. String Modification Methods
   - s.replace(old, new) : Replaces all occurrences of old with new. -> "hello world".replace("world", "Python") → "hello Python"
   - s.strip([chars])    : Removes leading & trailing characters.    -> " hello ".strip() → "hello"
   - s.lstrip([chars])   : Removes leading characters.               -> " hello ".lstrip() → "hello "
   - s.rstrip([chars])   : Removes trailing characters.              -> " hello ".rstrip() → " hello"

5. String Splitting and Joining Methods
   - s.split(sep)    : Splits the string into a list.     -> "apple,banana,grape".split(",") → ['apple', 'banana', 'grape']
   - s.rsplit(sep)   : Splits from the right side.       -> "a b c d".rsplit(" ", 2) → ['a b', 'c', 'd']
   - s.splitlines()  : Splits by line breaks.            -> "Hello\nWorld".splitlines() → ['Hello', 'World']
   - s.join(iterable): Joins elements of an iterable.    -> ", ".join(["apple", "banana"]) → "apple, banana"

6. Checking String Properties
   - s.startswith(prefix) : Checks if string starts with prefix.  -> "hello".startswith("he") → True
   - s.endswith(suffix)   : Checks if string ends with suffix.    -> "hello".endswith("lo") → True
   - s.isalpha()          : True if all characters are letters.   -> "Hello".isalpha() → True
   - s.isdigit()          : True if all characters are digits.    -> "1234".isdigit() → True
   - s.isalnum()          : True if all characters are alphanumeric. -> "Hello123".isalnum() → True
   - s.isspace()          : True if all characters are spaces.    -> "   ".isspace() → True
   - s.islower()          : True if all characters are lowercase. -> "hello".islower() → True
   - s.isupper()          : True if all characters are uppercase. -> "HELLO".isupper() → True
   - s.istitle()          : True if string follows title case.    -> "Hello World".istitle() → True

7. String Alignment Methods
   - s.center(width, fillchar) : Centers the string.  -> "hello".center(10, "-") → "--hello---"
   - s.ljust(width, fillchar)  : Left-aligns string.  -> "hello".ljust(10, "-") → "hello-----"
   - s.rjust(width, fillchar)  : Right-aligns string. -> "hello".rjust(10, "-") → "-----hello"
   - s.zfill(width)            : Pads string with leading zeros. -> "42".zfill(5) → "00042"

8. String Encoding & Decoding
   - s.encode(encoding) : Encodes string to bytes. -> "hello".encode() → b'hello'
   - s.decode(encoding) : Decodes bytes to string. -> b'hello'.decode() → "hello"

9. String Formatting Methods
   - s.format(*args)  : Formats string with placeholders. -> "My name is {}".format("Alice") → "My name is Alice"
   - f"{variable}"    : f-string (formatted string literals). -> name = "Bob"; f"Hello {name}" → "Hello Bob"
"""
