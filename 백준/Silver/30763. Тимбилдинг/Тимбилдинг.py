def solve():
    n, k = map(int,input().split())
    m = n // k
    if m >= k:
        print(0)
    else:
        q = k // m
        r = k % m
        print(m * (r * (q * (q + 1) // 2) + (m - r) * (q * (q - 1) // 2)))

solve()