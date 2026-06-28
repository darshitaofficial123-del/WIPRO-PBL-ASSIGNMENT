import sys

def is_prime(n: int) -> bool:
    """
    Checks whether a given number n is prime.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    # Expecting exactly 10 numbers as command line arguments
    if len(sys.argv) != 11:
        print("Usage: python script.py <num1> <num2> ... <num10>")
        return
    
    # Convert arguments to integers
    numbers = list(map(int, sys.argv[1:]))
    
    # Calculate sum of prime numbers
    prime_sum = sum(num for num in numbers if is_prime(num))
    
    print("Sum of prime numbers:", prime_sum)


if __name__ == "__main__":
    main()
