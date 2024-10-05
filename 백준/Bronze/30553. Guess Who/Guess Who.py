def guess_who(N, M, Q, attributes, questions):
    # Initialize a list of all characters
    possible_characters = list(range(N))  # Store indices of possible characters
    
    # Process each question
    for question in questions:
        A, response = question
        A -= 1  # Convert to 0-indexed
        
        # Filter possible characters based on the question
        possible_characters = [
            i for i in possible_characters
            if attributes[i][A] == response
        ]
    
    # Determine if the result is unique or ambiguous
    if len(possible_characters) == 1:
        return "unique", possible_characters[0] + 1  # Return index as 1-indexed
    else:
        return "ambiguous", len(possible_characters)

# Example input parsing
N, M, Q = map(int, input().split())
attributes = [input().strip() for _ in range(N)]
questions = [tuple(input().split()) for _ in range(Q)]
questions = [(int(A), response) for A, response in questions]

# Get result
result_type, result_value = guess_who(N, M, Q, attributes, questions)

# Output results
print(result_type)
print(result_value)