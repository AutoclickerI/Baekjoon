from itertools import permutations
for _ in[0]*int(input()):
    n=0
    m=10**9
    for _ in[0]*3:
        n<<=3
        t=0
        for i in input().split():t=(t<<1)+(i=='T')
        n+=t
    for i in permutations([7,56,448,73,146,292,273,84]):
        N=n
        for idx,j in enumerate(i):
            N^=j
            if N==0 or N==511:
                m=min(m,idx+1)
                break
    print(0 if n==0 or n==511 else -1 if m==10**9 else m)