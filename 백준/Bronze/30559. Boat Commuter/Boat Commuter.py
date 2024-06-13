def calculate_charges(n, m, k, events):
    current_tap = {}  # Keeps track of where each card last tapped
    charges = [0] * m  # Stores total charges for each card

    for p, c in events:
        card_index = c - 1
        if card_index in current_tap:
            start_pier = current_tap.pop(card_index)
            if start_pier == p:
                charges[card_index] += 100
            else:
                charges[card_index] += abs(start_pier - p)
        else:
            current_tap[card_index] = p

    # Apply penalties for unfinished trips
    for card_index in current_tap:
        charges[card_index] += 100

    return charges

# Example usage
n,m,k=map(int,input().split())
events = [[*map(int,input().split())]for _ in[0]*k]

print(*calculate_charges(n, m, k, events))