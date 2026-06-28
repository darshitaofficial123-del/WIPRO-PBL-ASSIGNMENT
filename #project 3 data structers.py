#project 3 data structers
#Count the frequency of words appearing in a string.

text = input("Enter a sentence: ")

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequencies:")
for word in frequency:
    print(word, ":", frequency[word])