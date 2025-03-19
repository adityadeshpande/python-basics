nums = {1, 2, 3, 3, 2}
print(nums)   

'''
A set is an unordered collection of unique elements. It is defined using curly braces {} or the set() function.
'''

fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)   

'''
Method	                Description
set.add(value)	        Adds an element to the set
set.remove(value)	    Removes an element (raises an error if not found)
set.discard(value)	    Removes an element (no error if not found)
set.pop()	            Removes and returns a random element
set.clear()	            Removes all elements
set.union(set2)	        Returns a new set with elements from both sets
set.intersection(set2)	Returns common elements between sets
set.difference(set2)	Returns elements in the first set but not in the second
'''

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s1.union(s2))   
print(s1.intersection(s2))   
print(s1.difference(s2))   
