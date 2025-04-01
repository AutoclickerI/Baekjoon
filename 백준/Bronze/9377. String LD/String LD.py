def solve():
    import sys
    input_data = sys.stdin.read().splitlines()
    idx = 0
    out_lines = []
    
    while idx < len(input_data):
        n = int(input_data[idx].strip())
        idx += 1
        if n == 0:
            break
        
        words = []
        for _ in range(n):
            words.append(input_data[idx].strip())
            idx += 1
        
        steps = 0
        while True:
            # Compute new list after left deletion
            new_words = [word[1:] if len(word) > 0 else "" for word in words]
            # Check for empty word
            if any(word == "" for word in new_words):
                break
            # Check for duplicates
            if len(set(new_words)) != len(new_words):
                break
            # If safe, update words and count step
            words = new_words
            steps += 1
        out_lines.append(str(steps))
        
    sys.stdout.write("\n".join(out_lines))
    
if __name__ == '__main__':
    solve()
