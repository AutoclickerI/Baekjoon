def solve():
    import sys
    input = sys.stdin.readline

    # Read number of cows and number of lines in the log.
    N, Nlines = map(int, input().split())
    
    # Initialize total time for each cow in minutes (1-indexed, cow i at index i)
    total_time = [0] * (N + 1)
    
    # Dictionary to store the start time (in minutes) for each cow
    start_time = {}
    
    for _ in range(Nlines):
        # Each entry: cow number, keyword, hour, minute
        parts = input().split()
        cow = int(parts[0])
        keyword = parts[1]
        hour = int(parts[2])
        minute = int(parts[3])
        time_in_minutes = hour * 60 + minute
        
        if keyword == "START":
            # Record start time for the cow.
            start_time[cow] = time_in_minutes
        elif keyword == "STOP":
            # Compute elapsed time and add to the cow's total.
            elapsed = time_in_minutes - start_time[cow]
            total_time[cow] += elapsed
            # Optionally remove the start time if needed.
            del start_time[cow]
    
    # Output each cow's total time as hours and minutes.
    for i in range(1, N + 1):
        hours = total_time[i] // 60
        minutes = total_time[i] % 60
        sys.stdout.write(f"{hours} {minutes}\n")

if __name__ == '__main__':
    solve()
