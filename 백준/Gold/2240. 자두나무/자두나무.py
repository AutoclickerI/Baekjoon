T,W,*l=map(int,open(0).read().split())
v=[0]*32
for i in l:
    for j in range(W+1):
        v[j]=max(v[j],v[j-1])+(j%2+1==i)
print(max(v))