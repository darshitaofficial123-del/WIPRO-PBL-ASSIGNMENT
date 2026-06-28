# Accept two numbers from the user and perform division.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except Exception as e:
    print("Error:", e)


# Accept a number from the user and check whether it is prime or not.
try:
    num = int(input("Enter a number: "))

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

except ValueError:
    print("Invalid Input! Please enter a number.")


# Accept the file name to be opened from the user.
try:
    filename = input("Enter file name: ")

    file = open(filename, "r")

    content = file.read()

    print(content.title())

    file.close()

except FileNotFoundError:
    print("File does not exist.")


# Declare a list with 10 integers and ask the user to enter an index.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

try:
    index = int(input("Enter index: "))

    if numbers[index] >= 0:
        print("Positive Number")
    else:
        print("Negative Number")

except IndexError:
    print("Invalid Index!")

except ValueError:
    print("Please enter a valid integer.")