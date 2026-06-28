def find_secret_message(filename: str):
    # Step 1: Read the file
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Step 2: Meeting time = number of lines
    num_lines = len(lines)

    # Convert to 12-hour format
    if num_lines == 0:
        print("File is empty, no meeting info.")
        return
    if num_lines <= 12:
        meeting_time = f"{num_lines} AM"
    else:
        hour = num_lines - 12
        meeting_time = f"{hour} PM"

    # Step 3: Find the most frequent word
    words = []
    for line in lines:
        for word in line.split():
            # Normalize by stripping punctuation
            word = word.strip(",.!?;:()[]\"'").lower()
            if word:
                words.append(word)

    # Count frequencies
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    # Find the word with maximum frequency
    meeting_place_word = max(freq, key=freq.get)
    meeting_place = meeting_place_word.capitalize() + " Street"

    # Step 4: Print results
    print("Meeting time:", meeting_time)
    print("Meeting place:", meeting_place)


# Sample usage
find_secret_message("Sample.txt")
