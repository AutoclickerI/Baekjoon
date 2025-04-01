T = int(input().strip())
for _ in range(T):
    sentence = input().strip().split()
    count = 0
    n = len(sentence)
    
    i = 0
    while i < n:
        word = sentence[i]
        # Check if the word is "u" or "ur"
        if word == "u" or word == "ur":
            count += 1
        
        # Check for "lol" substring in any word
        if "lol" in word:
            count += 1
        
        # Check for two-word sequences: "would of" or "should of"
        if i < n - 1:
            if (word == "would" or word == "should") and sentence[i+1] == "of":
                count += 1
        
        i += 1
    
    print(count * 10)
