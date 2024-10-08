for a in[0]*int(input()):
    n,m,c=map(int,input().split())
    *l,=map(int,input().split())
    for i in range(n+1-m):
        s=l[i:i+m]
        a+=max(s)-min(s)<=c
    print(a)