'''
Method	Description
append(x)	Adds x to the end of the list
remove(x)	Removes the first occurrence of x
sort()	    Sorts the list in ascending order
reverse()	Reverses the order of the list
pop(index)	Removes and returns the element at index
index(x)	Returns the index of the first occurrence of x
count(x)	Returns the count of x in the list
'''

numbers = [5, 3, 8, 1, 2]

numbers.append(10)
print(numbers)  

numbers.remove(3)
print(numbers)  

numbers.sort()
print(numbers)  

numbers.reverse()
print(numbers)  


# ---- What possibly can you do with a list?

fruits = ["apple", "banana", "cherry"]

# 1.

for fruit in fruits:
    print(fruit)

# 2.
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# --------------- Operate on list

numbers = [10, 5, 8, 23, 89, 3]
print(max(numbers)) 

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print(unique_numbers)   

numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(reversed_list) 


