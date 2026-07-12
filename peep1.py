def is_octal_string(s):
    # Check if all characters are between '0' and '7'
    return all(ch in '01234567' for ch in s)

# Given list of strings
strings = ['789', '123', '004']

# Check each string
for s in strings:
    if is_octal_string(s):
        print(f"'{s}' contains only octal digits.")
    else:
        print(f"'{s}' is NOT an octal string.")
