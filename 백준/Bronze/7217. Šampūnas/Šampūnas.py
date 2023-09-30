n,_,*l=map(int,open(0).read().split())
d=[0]*n
d[0]=1
for i in l:d[i-1]=1
for i in range(1,n):
    if d[i-1]==0:
        d[i]=1
print(sum(d))