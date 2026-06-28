# Add a key to a dictionary.
d = {0: 10, 1: 20}

d[2] = 30

print(d)


# Concatenate multiple dictionaries.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

result = {}

result.update(dic1)
result.update(dic2)
result.update(dic3)

print(result)


# Check if a given key already exists in a dictionary.
d = {1: "Apple", 2: "Banana", 3: "Mango"}

key = int(input("Enter key: "))

if key in d:
    print("Key exists")
else:
    print("Key does not exist")


# Iterate over dictionaries using for loops.
d = {
    1: "Apple",
    2: "Banana",
    3: "Mango"
}

for key in d:
    print(key, d[key])


# Generate and print a dictionary that contains a number (1 to n) in the form (x, x*x).
n = int(input("Enter n: "))

d = {}

for i in range(1, n + 1):
    d[i] = i * i

print(d)


# Sum all the values in a dictionary.
d = {
    "a": 100,
    "b": 200,
    "c": 300,
    "d": 400
}

total = sum(d.values())

print("Sum =", total)
