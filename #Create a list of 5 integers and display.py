#Create a list of 5 integers and display the list items. Access individual elements through index.
numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])


# Append a new item to the end of the list.
numbers = [10, 20, 30, 40, 50]

item = int(input("Enter new item: "))
numbers.append(item)

print(numbers)


# Reverse the order of the items in the list.
numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)


# Print the number of occurrences of a specified element in a list.
numbers = [10, 20, 30, 20, 40, 20, 50]

item = int(input("Enter element: "))

print(numbers.count(item))


# Append the items of list1 to list2 in the front.
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list2 = list1 + list2

print(list2)


# Insert a new item before the second element in an existing list.
numbers = [10, 20, 30, 40, 50]

item = int(input("Enter new item: "))

numbers.insert(1, item)

print(numbers)


# Remove the item from a specified index in a list.
numbers = [10, 20, 30, 40, 50]

index = int(input("Enter index: "))

numbers.pop(index)

print(numbers)


# Remove the first occurrence of a specified element from a list.
numbers = [10, 20, 30, 20, 40, 50]

item = int(input("Enter element: "))

numbers.remove(item)

print(numbers)