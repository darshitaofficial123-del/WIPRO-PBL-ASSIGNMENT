def append_to_file(filename: str):
    """
    Accepts input from the user and appends it to a text file.
    """
    try:
        # Get user input
        user_text = input("Enter text to append to the file: ")

        # Open file in append mode
        with open(filename, 'a') as f:
            f.write(user_text + "\n")

        print(f"Text successfully appended to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Sample usage
append_to_file("Sample.txt")
