for T in range(int(input())):
    m, n = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    ans = 0
    for _ in range(n):
        h, w, d, i = map(int, input().split())
        ans += h * w * d * a[i-1]
    print(f'Data Set {T+1}:\n{ans}')