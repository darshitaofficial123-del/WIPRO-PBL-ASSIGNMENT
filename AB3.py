import sys

def main():
    # sys.argv[0] is always the script file name
    file_name = sys.argv[0]

    # Check if a welcome message is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <welcome_message>")
        return

    # Join all arguments after the file name as the welcome message
    welcome_message = " ".join(sys.argv[1:])

    # Display file name and welcome message
    print("File Name:", file_name)
    print("Welcome Message:", welcome_message)


if __name__ == "__main__":
    main()
