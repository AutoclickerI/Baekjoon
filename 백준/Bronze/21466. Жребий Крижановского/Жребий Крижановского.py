def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    # Scores of all players before the last round (Petya is last)
    scores = list(map(int, data[1:n+1]))
    # Numbers chosen by the first n-1 players in the last round
    others = list(map(int, data[n+1:n+1+(n-1)]))
    
    best_count = -1
    best_candidate = None

    # We simulate candidate choices for Petya from 1 to 1000.
    # (1000 is a safe upper bound for this problem's constraints.)
    for x in range(1, 1001):
        # Create the list of numbers chosen in the round including Petya's candidate x.
        chosen = others + [x]
        freq = {}
        for num in chosen:
            freq[num] = freq.get(num, 0) + 1

        # Make a copy of initial scores to simulate round outcome.
        final_scores = scores[:]
        # Determine the winner if there is any unique number.
        # If no unique number exists, the round is a draw.
        unique_nums = [num for num in chosen if freq[num] == 1]
        if unique_nums:
            # The winning number is the smallest unique number.
            winning_number = min(unique_nums)
            # Find the first occurrence of winning_number.
            winner_index = chosen.index(winning_number)
            # The winner gets bonus points equal to winning_number.
            final_scores[winner_index] += winning_number

        # Count how many other players end up with a final score strictly less than Petya's.
        petya_final = final_scores[-1]
        count = sum(1 for i in range(n - 1) if final_scores[i] < petya_final)

        # Update candidate: maximize count, tie-break with minimal candidate number.
        if count > best_count or (count == best_count and (best_candidate is None or x < best_candidate)):
            best_count = count
            best_candidate = x

    print(best_candidate)


if __name__ == '__main__':
    main()
