*p,=range(2*10**5)
for i in range(2,2*10**5):
    if p[i]:
        t=2*i
        while t<len(p):
            p[t]=0
            t+=i
N=int(input())
l=[[*map(int,input().split())]for _ in[0]*N*N]
prime=[*{i for i in p[2:] if i}-{*sum(l,[])}]
for i in range(N*N):
    for j in range(N*N):
        l[i][j]=l[i][j]or prime.pop()
for i in l:
    print(*i)