N,H,*l=map(int,open(0).read().split())
d={i:l.count(i)for i in l}
l=[0,1]
for i in range(H):
    l+=0,
    for j in d:x=2+i-j;l[-1]+=0<x and d[j]*l[x]
    l[-1]%=10**9+7
print(l[-1])