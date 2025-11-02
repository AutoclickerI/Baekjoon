N,*l=map(int,open(0).read().split())
c=[0]*N
for i in range(N):
    for j in range(i+1,N):
        f=1
        for k in range(i+1,j):
            if (l[j]-l[i])*k+(j*l[i]-i*l[j])<=l[k]*(j-i):
                f=0
        c[i]+=f
        c[j]+=f

print(max(c))