def sort_colors(color_sequence: str) -> str:
    """
    Accepts a hyphen-separated sequence of colors as input
    and returns them sorted alphabetically in the same format.
    """
    # Split the input string into a list
    colors = color_sequence.split('-')
    
    # Sort the list alphabetically
    colors.sort()
    
    # Join the sorted list back into a hyphen-separated string
    return '-'.join(colors)


# Sample usage
print(sort_colors("green-red-yellow-black-white"))  
# Output: black-green-red-white-yellow

print(sort_colors("PINK-BLUE-TAN-PURPLE"))  
# Output: BLUE-PINK-PURPLE-TAN
