# name_utils.py

def ispalindrome(name: str) -> str:
    """
    Checks if the given name is a palindrome.
    Returns a message string.
    """
    if name == name[::-1]:
        return "Yes it is a palindrome."
    else:
        return "No it is not a palindrome."


def count_the_vowels(name: str) -> str:
    """
    Counts the number of vowels in the given name.
    Returns a message string.
    """
    vowels = "aeiouAEIOU"
    count = sum(1 for ch in name if ch in vowels)
    return f"No of vowels: {count}"


def frequency_of_letters(name: str) -> str:
    """
    Calculates the frequency of each letter in the given name.
    Returns a formatted string.
    """
    freq = {}
    for ch in name:
        freq[ch] = freq.get(ch, 0) + 1
    
    # Format as "letter-count" pairs separated by commas
    freq_str = ", ".join([f"{ch}-{count}" for ch, count in freq.items()])
    return f"Frequency of letters: {freq_str}"
