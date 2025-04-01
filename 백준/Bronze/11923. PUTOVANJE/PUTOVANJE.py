def solve():
    import sys
    input = sys.stdin.readline

    # Number of fruits and capacity
    N, C = map(int, input().split())
    fruits = list(map(int, input().split()))
    
    max_count = 0
    # Try starting from each fruit
    for start in range(N):
        total = 0
        count = 0
        # Simulate eating from the current starting index
        for i in range(start, N):
            if total + fruits[i] <= C:
                total += fruits[i]
                count += 1
        max_count = max(max_count, count)
    
    print(max_count)

if __name__ == '__main__':
    solve()
