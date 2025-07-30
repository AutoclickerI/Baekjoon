n,*l=map(int,open(0).read().split())
z=l[:]
c=v=0
for i in range(n-1):
    if i%2:
        if l[i]<=l[i+1]:
            l[i+1]=-1e9
            c+=1
        if z[i]>=z[i+1]:
            z[i+1]=1e9
            v+=1
    else:
        if l[i]>=l[i+1]:
            l[i+1]=1e9
            c+=1
        if z[i]<=z[i+1]:
            z[i+1]=-1e9
            v+=1
print(min(c,v))