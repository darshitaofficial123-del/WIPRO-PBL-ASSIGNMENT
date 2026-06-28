def read_file(filename: str):
    """
    Reads the entire content from a text file and displays it.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print("File Content:\n")
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Sample usage
read_file("Sample.txt")
