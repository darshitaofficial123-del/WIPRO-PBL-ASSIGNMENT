# Count the number of upper and lower case letters in a string.
text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# Count the number of strings where the string length is 2 or more and the first and last characters are the same.
words = ["abc", "xyz", "aba", "1221"]

count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("Count:", count)


# Get a string made of the first 2 and the last 2 characters of a given string.
text = input("Enter a string: ")

if len(text) < 2:
    print("")
else:
    print(text[:2] + text[-2:])


# Get a string from a given string where all occurrences of its first character have been changed to '$', except the first character itself.
text = input("Enter a string: ")

first = text[0]

new_text = first + text[1:].replace(first, "$")

print(new_text)


# Get a single string from two given strings separated by a space and swap the first two characters of each string.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

print(new_str1 + " " + new_str2)