for i in range(int(input())):
    L,N=map(int, input().split())
    a=p=0
    d = 'C'
    for _ in range(N):
        D, C = input().split()
        D = int(D)
        
        if C == d:
            c, p = divmod(p + D, L)
        else:
            c, p = divmod(-p + D, L)
            if c != -1:
                d = C
        a += c
    print(f"Case #{i+1}: {a}")