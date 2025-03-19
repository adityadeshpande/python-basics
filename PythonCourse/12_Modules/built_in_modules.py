'''
Python has many built-in modules like math, random, and datetime.
'''
import math
print(math.sqrt(25))   
print(math.pi)      

from math import sqrt, pi
print(sqrt(16))  
print(pi)        


import random
print(random.randint(1, 100))  
print(random.choice(["apple", "banana", "cherry"]))  
print(random.shuffle([1, 2, 3, 4, 5]))


import datetime
now = datetime.datetime.now()
print(now)  
print(now.strftime("%Y-%m-%d %H:%M:%S"))  

# -------------------------------------------------------------------------------
## used in DS and mathematics and stuff

'''
numpy – Numerical Computing
NumPy is used for working with arrays and numerical computations
'''
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr * 2)   

'''
pandas – Data Analysis
Pandas is used for data manipulation and analysis
'''
import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)


'''
matplotlib – Data Visualization
Matplotlib is used for plotting graphs and charts
'''
# import matplotlib.pyplot as plt 

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# plt.plot(x, y, marker='o')
# plt.title("Sample Graph")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()
