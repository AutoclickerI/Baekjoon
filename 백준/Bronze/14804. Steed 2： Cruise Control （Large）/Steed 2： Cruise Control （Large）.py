def solve():
    import sys
    input = sys.stdin.readline
    T = int(input().strip())
    
    for t in range(1, T+1):
        D, N = map(int, input().split())
        max_time = 0.0
        
        for _ in range(N):
            K, S = map(int, input().split())
            time = (D - K) / S
            if time > max_time:
                max_time = time
        
        # Annie's maximum constant speed is D divided by the slowest horse's time.
        result = D / max_time
        sys.stdout.write("Case #{}: {:.6f}\n".format(t, result))

if __name__ == '__main__':
    solve()
