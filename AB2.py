import sys

def main():
    # Check if exactly 2 arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <num1> <num2>")
        return
    
    # Convert arguments to integers
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    
    # Calculate sum
    result = num1 + num2
    
    # Display result
    print("Sum:", result)

if __name__ == "__main__":
    main()
