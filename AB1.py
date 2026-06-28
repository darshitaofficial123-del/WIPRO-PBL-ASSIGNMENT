import sys

def calculate_happiness(likes: str, dislikes: str, given: str) -> int:
    """
    Calculate happiness based on liked and disliked numbers.
    """
    # Convert hyphen-separated strings into sets/lists of integers
    like_set = set(map(int, likes.split('-')))
    dislike_set = set(map(int, dislikes.split('-')))
    given_numbers = list(map(int, given.split('-')))

    happiness = 0
    for num in given_numbers:
        if num in like_set:
            happiness += 1
        elif num in dislike_set:
            happiness -= 1
        # else: no change
    return happiness


if __name__ == "__main__":
    # Command line arguments: sys.argv[1], sys.argv[2], sys.argv[3]
    if len(sys.argv) != 4:
        print("Usage: python script.py <likes> <dislikes> <given>")
        sys.exit(1)

    likes = sys.argv[1]
    dislikes = sys.argv[2]
    given = sys.argv[3]

    result = calculate_happiness(likes, dislikes, given)
    print(result)
