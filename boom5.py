def read_lines_to_list(filename: str):
    """
    Reads contents from a text file line by line
    and stores each line into a list.
    """
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        # Strip newline characters
        lines = [line.strip() for line in lines]
        
        print("Lines stored in list:")
        print(lines)
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Sample usage
read_lines_to_list("Sample.txt")
