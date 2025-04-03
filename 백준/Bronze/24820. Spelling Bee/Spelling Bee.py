def main():
    import sys
    data = sys.stdin.read().split()
    
    # First 7 letters: first is center
    letters = data[0]
    center = letters[0]
    allowed = set(letters)
    
    n = int(data[1])
    words = data[2:]
    
    # Filter words that meet all conditions:
    # - at least 4 letters long
    # - contains the center letter
    # - uses only letters from the allowed set
    results = []
    for word in words:
        if len(word) >= 4 and center in word and set(word).issubset(allowed):
            results.append(word)
    
    # Print results in the same order as in the dictionary input.
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    main()
