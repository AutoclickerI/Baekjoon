def is_valid_set(card1, card2, card3):
    for i in range(4):  # There are 4 characteristics
        if not (card1[i] == card2[i] == card3[i] or 
                len({card1[i], card2[i], card3[i]}) == 3):
            return False
    return True

# Read input
cards = []
for _ in range(4):
    line = input().strip().split()
    cards.extend(line)

sets_found = []

# Find all sets of cards
for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        for k in range(j + 1, len(cards)):
            if is_valid_set(cards[i], cards[j], cards[k]):
                sets_found.append(sorted([i + 1, j + 1, k + 1]))  # Store 1-based indices

# Sort found sets by the first, second, and then third card number
sets_found.sort()

# Output results
if sets_found:
    for s in sets_found:
        print(" ".join(map(str, s)))
else:
    print("no sets")