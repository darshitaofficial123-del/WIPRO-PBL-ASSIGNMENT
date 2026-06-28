# Create a set.
s = {10, 20, 30, 40, 50}

print(s)


# Iterate over sets.
s = {10, 20, 30, 40, 50}

for i in s:
    print(i)


# Add member(s) to a set.
s = {10, 20, 30}

item = int(input("Enter new item: "))

s.add(item)

print(s)


# Remove item(s) from a set.
s = {10, 20, 30, 40, 50}

item = int(input("Enter item to remove: "))

s.remove(item)

print(s)