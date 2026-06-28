def find_longest_word(filename: str):
    """
    Reads contents from a text file and finds the longest word.
    Assumes there is only one longest word in the file.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()

        # Split into words and strip punctuation
        words = [word.strip(",.!?;:()[]\"'") for word in content.split()]

        # Find the longest word
        longest_word = max(words, key=len)

        print("Longest word in the file:", longest_word)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Sample usage
find_longest_word("Sample.txt")
