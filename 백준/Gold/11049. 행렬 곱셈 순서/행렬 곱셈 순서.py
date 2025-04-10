N=int(input())
l=[[*map(int,input().split())]for _ in[0]*N]

d=[N*[0]for _ in[0]*N]

# minimum value needed to multiply from s to e
def f(s,e):
    if d[s][e]:
        return d[s][e]
    if s==e:
        return 0
    minval=1e18
    for m in range(s,e):
        v1=f(s,m)
        v2=f(m+1,e)
        val=v1+v2+l[s][0]*l[m][1]*l[e][1]
        if val<minval:
            minval=val
    d[s][e]=minval
    return minval

print(f(0,N-1))