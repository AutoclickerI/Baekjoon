# Define the key mapping (which key, how many presses for each letter)
key_mapping = {
    'a': (2, 1), 'b': (2, 2), 'c': (2, 3),
    'd': (3, 1), 'e': (3, 2), 'f': (3, 3),
    'g': (4, 1), 'h': (4, 2), 'i': (4, 3),
    'j': (5, 1), 'k': (5, 2), 'l': (5, 3),
    'm': (6, 1), 'n': (6, 2), 'o': (6, 3),
    'p': (7, 1), 'q': (7, 2), 'r': (7, 3), 's': (7, 4),
    't': (8, 1), 'u': (8, 2), 'v': (8, 3),
    'w': (9, 1), 'x': (9, 2), 'y': (9, 3), 'z': (9, 4),
}

def calculate_time(word):
    time = 0
    last_key = None

    for letter in word:
        key, presses = key_mapping[letter]
        time += presses  # Add time for presses

        # If the current key is the same as the last key, add a pause
        if last_key == key:
            time += 2

        last_key = key  # Update last key to current key

    return time

# Input reading loop
while True:
    word = input().strip()
    
    if word == "halt":
        break
    
    # Calculate and print the time for each word
    print(calculate_time(word))