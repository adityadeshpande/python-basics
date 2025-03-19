person = {"name": "John", "age": 25}
print(person["name"])


student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science"
}
print(student) 
print(student["name"])  
print(student.get("age"))

### why use Get() instead of  []
# print(student.get("grade"))
# print(student["grade"])  

# ----------- What can you do with a dict---------
'''
Method	                Description
dict.get(key, default)	Returns value for key, or default if key is not found
dict.keys()	            Returns all keys as a list-like object
dict.values()	        Returns all values as a list-like object
dict.items()	        Returns key-value pairs as tuples
dict.update(new_dict)	Updates dictionary with key-value pairs from another dictionary
dict.pop(key)	        Removes and returns the value of key
dict.clear()	        Removes all key-value pairs
'''

# --- Play around ---
''' 
print(student.keys())  
print(student.values())  
print(student.items())   

student["age"] = 23  
student["grade"] = "A"  
print(student)   

student.pop("course")   
print(student)

student.clear()   
print(student)

'''