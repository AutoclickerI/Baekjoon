p,q=map(int,input().split())
r,s=map(int,input().split())
l=[p/r+q/s,r/s+p/q,s/q+r/p,q/p+s/r]
print(l.index(max(l)))