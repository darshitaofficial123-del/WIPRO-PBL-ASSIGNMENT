def factorial(n: int) -> int:
    """
    Returns the factorial of a non-negative integer n.
    Factorial of n (denoted n!) is the product of all positive integers ≤ n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Sample usage
print(factorial(5))   # Expected Output: 120
print(factorial(0))   # Expected Output: 1
print(factorial(7))   # Expected Output: 5040
