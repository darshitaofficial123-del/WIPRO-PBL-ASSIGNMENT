def print_even_numbers(numbers: list) -> None:
    """
    Accepts a list of numbers and prints the even numbers.
    """
    even_numbers = [num for num in numbers if num % 2 == 0]
    print(even_numbers)


# Sample usage
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(sample_list)  
# Expected Result: [2, 4, 6, 8]
