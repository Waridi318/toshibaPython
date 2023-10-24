# list are Ordered
fruits = ["mangoes", "Oranges", "Bananas", "Watermelon", 67]
# fruits.sort()
num = [11, 3, 7, 0, 14, 4, -3, 2]
num.sort()
num[3] = 9
rep = num * 2
# print(len(num))

print(fruits)
fruits[1] = "apples"
print(f"I Love eating {fruits[1]}")
# print(num)
print(sorted(num))
print(rep)

# Tuples immutable (cannot add elements) ordered
cars = ("Toyota", "Mercedes", "Nissan", "Nissan")
# cars[0] = "vw"
tuplep = cars * 3
print(tuplep)
print(tuplep.count(2))
print(tuplep.count("Nissan"))

# Sets (Unordered) Does not have index
days = {"Monday", "Tuesday", "Wednesday", "Thurday", "Friday"}
print(days)

# dictionaries (Dict)
staff_details = {"Name ": "Kennedy", "Age": 27, "Company": "Bluechange", "Salary": 50000}
print(staff_details)
print("Name: %s" % staff_details["Name "])
print("salary: %s" % staff_details["Salary"])
print("Age: %s" % staff_details["Age"])
print("Company: %s" % staff_details["Company"])
