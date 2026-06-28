def count_case(s: str) -> None:
    """
    Accepts a string and prints the number of uppercase
    and lowercase letters in it.
    """
    upper_count = 0
    lower_count = 0
    
    for ch in s:
        if ch.isupper():
            upper_count += 1
        elif ch.islower():
            lower_count += 1
    
    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case characters:", lower_count)


# Sample usage
sample_str = "Hello World!"
count_case(sample_str)
