N,P=map(int,input().split())
*x,v=map(int,input().split())
V=N
l=[0]*P
l[0]=v
for i in x:
    l[(V-1)%(P-1)+1]=(l[(V-1)%(P-1)+1]+i)%P
    V-=1
for i in range(P):
    print((l[0]+sum(l[(j-1)%(P-1)+1]*pow(i,j,P)for j in range(1,P)))%P)