# Input list
input_list = [1, 2, 3, 4, 5, 6, 7]

# Dictionary comprehension: odd numbers as keys, cubes as values
output_dict = {x: x**3 for x in input_list if x % 2 != 0}

print(output_dict)
