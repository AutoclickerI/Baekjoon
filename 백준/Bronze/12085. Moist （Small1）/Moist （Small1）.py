def solve():
    import sys
    input = sys.stdin.readline
    
    T = int(input().strip())
    for t in range(1, T + 1):
        N = int(input().strip())
        # Read the deck in order (top to bottom)
        deck = [input().rstrip('\n') for _ in range(N)]
        
        cost = 0
        # Start with the first card in our "sorted" deck.
        sorted_deck = [deck[0]]
        
        # Process the rest of the cards one by one.
        for card in deck[1:]:
            # If the card is lexicographically not less than the last card,
            # then it's in the right order and we just add it.
            if card >= sorted_deck[-1]:
                sorted_deck.append(card)
            else:
                # Otherwise, the robot moves this card (cost $1)
                cost += 1
                # Find the correct insertion position in sorted_deck
                # so that sorted_deck remains in lexicographical order.
                pos = 0
                while pos < len(sorted_deck) and sorted_deck[pos] <= card:
                    pos += 1
                sorted_deck.insert(pos, card)
                
        sys.stdout.write(f"Case #{t}: {cost}\n")

if __name__ == '__main__':
    solve()
