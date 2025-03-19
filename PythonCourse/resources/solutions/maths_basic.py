def find_maximum(n, arr):
    max_val = max(arr)
    print(max_val)
    
def find_minimum1(n, arr):
    min_val = arr[0]  
    for num in arr:
        if num < min_val:
            min_val = num
    print(min_val)   
    
def find_minimum(n, arr):   
    min_val = min(arr)
    print(min_val)
    
def fizz_buzz(num):
  for i in range(1,num+1):
      output = ""
      if (i % 3 == 0):
        output += "Fizz"
      if (i % 5 == 0):
        output += "Buzz"
      print(output if output else i)
      
      
def is_prime(num):
    if num < 2:  # Handle numbers < 2
        print("No")
        return
    isprimeNum = True
    for i in range(2, num): 
        if num % i == 0:
            isprimeNum = False
            break  # Exit early when a factor is found
    print("Yes" if isprimeNum else "No")

def is_palindrome(Str):
  print("Yes" if Str == Str[::-1] else "No")

def character_frequency(n, s):
    freq = {}  
    order = []  
    
    for char in s:
        if char not in freq:
            freq[char] = 0
            order.append(char)  
        freq[char] += 1

    for char in order:
        print(char, freq[char])
        
        
def runCode():
    character_frequency(10, "zbcdazallz")
        
        
runCode()