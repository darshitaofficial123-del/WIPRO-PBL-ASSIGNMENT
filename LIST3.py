import string

# Create dictionary mapping a-z to 1-26
alphabet_dict = {letter: idx+1 for idx, letter in enumerate(string.ascii_lowercase)}

print(alphabet_dict)
