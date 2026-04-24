for T in[0]*int(input()):
    N=int(input())
    l=sorted([*map(int,input().split())]for _ in[0]*N)[::-1]
    s=[*map(int,input().split())]
    r=0
    f=1
    for i in range(N):
        f&=0<=s[i]
        r+=s[i]
        s=[j-s[i]*k for j,k in zip(s,l[i])]
    f&=r<=2*10**9
    print(*[f,r][:f+1])