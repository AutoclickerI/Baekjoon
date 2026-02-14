for _ in[0]*int(input()):
    n=int(input())
    *l,=map(int,input().split())
    c=1
    while sum(l)<=n:
        c+=1
        t=l[:]
        for i in range(6):
            t[i]+=l[i-1]+l[i-3]+l[i-5]
        l=t
    print(c)