def windows_overlap(r1, c1, w1, h1, r2, c2, w2, h2):
    # Check horizontal overlap
    horizontal_overlap = not (c1 + w1 <= c2 or c2 + w2 <= c1)
    # Check vertical overlap
    vertical_overlap = not (r1 + h1 <= r2 or r2 + h2 <= r1)
    # If both horizontal and vertical overlap, then windows overlap
    return horizontal_overlap and vertical_overlap

def count_overlapping_windows(windows):
    n = len(windows)
    overlap_count = 0
    # Track which windows overlap
    overlap_flags = [False] * n
    for i in range(n):
        r1, c1, w1, h1 = windows[i]
        for j in range(i + 1, n):
            r2, c2, w2, h2 = windows[j]
            if windows_overlap(r1, c1, w1, h1, r2, c2, w2, h2):
                overlap_flags[i] = True
                overlap_flags[j] = True
    # Count how many windows have been marked as overlapping
    return sum(overlap_flags)

# Main loop to process multiple test cases
while True:
    n = int(input())
    if n == 0:
        break
    windows = [tuple(map(int, input().split())) for _ in range(n)]
    result = count_overlapping_windows(windows)
    print(result)