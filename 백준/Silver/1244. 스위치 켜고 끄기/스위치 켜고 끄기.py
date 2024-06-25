n=int(input())
*l,=map(int,input()[::2])
for _ in[0]*int(input()):
    p,q=map(int,input().split())
    if p<2:
        for i in range(q-1,n,q):l[i]^=1
    else:
        s,e=q-1,q
        while 0<=s<e<=n and l[s:e]==l[s:e][::-1]:
            s-=1
            e+=1
        s+=1
        e-=1
        for i in range(s,e):l[i]^=1
while l:
    print(*l[:20])
    l=l[20:]