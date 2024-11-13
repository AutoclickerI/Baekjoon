_,*l=map(int,open(0).read().split())
m=max(l[::2])
M=min(l[1::2])
print(*['bad news']*(M<m)or[M-m+1,m])