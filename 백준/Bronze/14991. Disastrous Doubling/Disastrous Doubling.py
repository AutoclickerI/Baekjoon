def disastrous_doubling(n, b):
    MOD = 10**9+7
    B = max(b)
    cur = 1
    split = -1

    for i, bi in enumerate(b):
        cur <<= 1
        if cur < bi:
            return "error"
        cur -= bi
        if cur >= B:
            split = i
            break

    if split < 0:
        return str(cur % MOD)

    # tail-sum mod
    R = cur % MOD
    pow2 = pow(2, n - (split+1), MOD)
    ans = R * pow2 % MOD

    tail = 0
    for j in range(split+1, n):
        tail = (tail + (b[j] % MOD) * pow(2, (n-1)-j, MOD)) % MOD

    ans = (ans - tail) % MOD
    return str(ans)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    b = list(map(int, input().split()))
    print(disastrous_doubling(n, b))
