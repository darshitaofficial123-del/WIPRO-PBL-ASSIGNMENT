import re

sentence = """A, very   very; irregular_sentence"""

# Replace punctuation with spaces, then split
words = re.split(r'[\s,;_]+', sentence.strip())

# Filter out any empty strings
words = [w for w in words if w]

print(words)
