d={}
for _ in[0]*int(input()):
    p,q=input().split()
    d[q]=-int(p)
for _ in[0]*int(input()):
    x,y,z=input().split()
    tmp=d[y]-15*([.5,0,1][int(z)]-1/(1+10**((d[y]-d[x])/400)))
    d[x]=min(int(d[x]-15*([.5,1,0][int(z)]-1/(1+10**((d[x]-d[y])/400)))),0)
    d[y]=min(int(tmp),0)
for i,j in sorted((d[i],i)for i in d):
    print(-i,j)