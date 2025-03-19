coordinates_tupl = (10, 20)
coordinates_list = [10, 20]
print(coordinates_tupl[1])


colors = ("red", "green", "blue")
numbers = (1, 2, 3, 4, 5)

print(colors[0])   
print(colors[-1])  


x, y, z = colors
print(x)  



mixed_keys = ("name", "fruit", "weight", "count", "isAvailable")
mixed = ("jack","apple", 54.32, 110, False)

for key in mixed_keys:
    index = mixed_keys.index(key) 
    value = mixed[index]           
    print(f"{key}: {value}")
