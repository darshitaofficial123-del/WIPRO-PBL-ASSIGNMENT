def count_word_frequency(filename: str):
    """
    Reads a text file and counts the frequency of a user-entered word.
    """
    try:
        # Ask user for the word to search
        search_word = input("Enter the word to count: ").strip().lower()

        with open(filename, 'r') as f:
            content = f.read()

        # Normalize words by stripping punctuation and converting to lowercase
        words = [word.strip(",.!?;:()[]\"'").lower() for word in content.split()]

        # Count frequency
        frequency = words.count(search_word)

        print(f"The word '{search_word}' appears {frequency} times in {filename}.")
    except FileNot