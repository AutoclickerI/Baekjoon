def calc(a, b, c, v):
    try:
        idx_a = v.index(a)
        idx_b = v.index(b)
        return c if idx_a < idx_b else int(1e9)
    except ValueError:
        return int(1e9)

def solve():
    a, b, n = map(int, input().split())
    ans = int(1e9)
    
    for _ in range(n):
        c,k = map(int, input().split())
        *rest, = map(int, input().split())
        if len(rest) < k:
            rest += list(map(int, input().split()))
        v = rest[:k]
        ans = min(ans, calc(a, b, c, v))

    print(-1 if ans == int(1e9) else ans)

if __name__ == "__main__":
    solve()