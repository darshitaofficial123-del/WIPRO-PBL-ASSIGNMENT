# Create a tuple with different data types.
t = (10, 3.14, "Python", True)

print(t)


# Create a tuple with numbers and print one item.
t = (10, 20, 30, 40, 50)

index = int(input("Enter index: "))

print(t[index])


# Add an item to a tuple.
t = (10, 20, 30)

item = int(input("Enter new item: "))

t = t + (item,)

print(t)


# Convert a tuple to a string.
t = ('P', 'Y', 'T', 'H', 'O', 'N')

s = ""

for i in t:
    s = s + i

print(s)


# Find the length of a tuple.
t = (10, 20, 30, 40, 50)

print("Length =", len(t))