words = ["civic", "trust", "widows", "maximum", "museums", "aa", "as"]

# Filter words where first and last character match
result = [w for w in words if w[0] == w[-1]]

print(result)
