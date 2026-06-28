def is_prime(n: int) -> bool:
    """
    Checks whether a given number n is prime.
    Returns True if prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisibility up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Sample usage
num1 = 7
print(f"{num1} is prime? {is_prime(num1)}")  # Expected: True

num2 = 10
print(f"{num2} is prime? {is_prime(num2)}")  # Expected: False

num3 = 1
print(f"{num3} is prime? {is_prime(num3)}")  # Expected: False
