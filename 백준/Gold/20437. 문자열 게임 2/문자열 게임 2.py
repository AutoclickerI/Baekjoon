for _ in[0]*int(input()):
    s=input()
    v=[[]for _ in[0]*26]
    for i in range(len(s)):
        v[ord(s[i])-97]+=i,
    t1=float('inf')
    t2=0
    K=int(input())
    for c in v:
        for i in range(len(c)-K+1):
            t1=min(t1,c[i+K-1]-c[i]+1)
            t2=max(t2,c[i+K-1]-c[i]+1)
    if t1==float('inf'):
        print(-1)
    else:
        print(t1,t2)