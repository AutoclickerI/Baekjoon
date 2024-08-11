import sys
input=sys.stdin.readline
def find_parallel_fifths(N, notes):
    if N == 0:
        return ["POLE"]
    
    parallel_fifths_indices = []
    
    for i in range(1, N):
        diff1 = notes[i-1][0] - notes[i-1][1]
        diff2 = notes[i][0] - notes[i][1]
        
        # Check if both intervals are a perfect fifth (7 semitones)
        if diff1 % 12 == 7 and diff2 % 12 == 7:
            # Check if there is a pitch change in both voices
            if (notes[i-1][0] != notes[i][0]) and (notes[i-1][1] != notes[i][1]):
                parallel_fifths_indices.append(i)
    
    if not parallel_fifths_indices:
        return ["POLE"]
    
    return [str(index) for index in parallel_fifths_indices]

# Input handling
N = int(input())
notes = [tuple(map(int, input().split())) for _ in range(N)]

# Function call
result = find_parallel_fifths(N, notes)

# Output results
print("\n".join(result))