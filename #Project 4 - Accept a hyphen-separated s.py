#Project 4 - Accept a hyphen-separated sequence of words, sort them alphabetically, and print them.

text = input("Enter hyphen-separated words: ")

words = text.split("-")

words.sort()

result = "-".join(words)

print(result)