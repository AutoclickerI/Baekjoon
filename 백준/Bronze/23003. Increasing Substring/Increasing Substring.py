for T in range(int(input())):
    N = int(input())
    S = input()
    buf = [1]
    cur = 1
    for i in range(1, N):
        if S[i] > S[i-1]:
            cur += 1
        else:
            cur = 1
        buf+=cur,
    print(f'Case #{T+1}:', *buf)