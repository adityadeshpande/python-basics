# Slicing is a way to extract a subset of a sequence 
# (like a list, tuple, or string) using the syntax:
'''
    sequence[start:stop:step]
    
    start → The index where the slice begins (inclusive).
    stop → The index where the slice ends (exclusive).
    step → (Optional) The interval between elements.
'''

fruits = ["apple", "banana", "cherry", "date", "plum"]
print(fruits[1:3])  

# if you omit 'start' it's considered default 0
print(fruits[:3])  

# if you omit 'stop' it's considered default to end of list
print(fruits[2:])  


#Using Negative Indexing
'''
-3 → "cherry"
-1 → "elderberry" (exclusive, so not included)
'''
print(fruits[-3:-1]) 

#using the step!!
print(fruits[0:5:2])   


#reversing a list using slicing
print(fruits[::-1])  
    #       [::-1] means start from the end and move backward.





# --- TRY IT ---
def middle_three(lst):
    mid = len(lst) // 2
    return lst[mid - 1 : mid + 2]  # Extracting 3 elements centered around mid

nums = [1, 2, 3, 4, 5, 6, 7]
print(middle_three(nums))  
