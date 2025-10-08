[N],*l=[map(int,i.split())for i in open(0)]
p=[0]*-~N
for i in range(N):
    p[i]=max(p[i],p[i-1])
    t,c=l[i]
    if i+t<=N:
        p[i+t]=max(p[i+t],p[i]+c)
print(max(p))