def read_first_n_lines(filename: str, n: int):
    """
    Reads the first n lines from a text file and displays them.
    """
    try:
        with open(filename, 'r') as f:
            # Read all lines
            lines = f.readlines()
            
            # Slice the first n lines
            first_n = lines[:n]
            
            print(f"First {n} lines from {filename}:\n")
            for line in first_n:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Sample usage
filename = "Sample.txt"
n = int(input("Enter the number of lines to read: "))
read_first_n_lines(filename, n)
