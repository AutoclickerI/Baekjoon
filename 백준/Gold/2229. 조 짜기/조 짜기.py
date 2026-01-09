n,*l=map(int,open(0).read().split())
z=[0]
for i in range(n):
    mv=0
    for j in range(i+1):
        t=z[j]+max(l[j:i+1])-min(l[j:i+1])
        mv=max(mv,t)
    z+=mv,
print(z[-1])