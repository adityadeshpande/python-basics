import csv
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])  # header
    writer.writerow(["Alice", 25, "New York"])
    writer.writerow(["Bob", 30, "London"])


import csv
with open("data.csv", newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Each row is a list
