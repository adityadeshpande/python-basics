

def add(a, b):
    print(f"Adding {a} and {b}")  #Print Statements for Debugging
    return a + b

print(add(3, 4))



''' !!! Assertions are great for debugging but should be removed in production. !!! '''
# Using assert 
def divide(a, b):
    assert b != 0, "Denominator cannot be zero!"
    return a / b

print(divide(10, 2))
# print(divide(10, 0))


import pdb
def test_function(x):
    pdb.set_trace()  # Debugging starts here
    y = x + 10
    return y

print(test_function(5))


import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
