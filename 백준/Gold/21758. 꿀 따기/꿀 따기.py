s,*l=map(int,[*open(0)][1].split())
d=[s]
for i in l:d+=d[-1]+i,
*_,x,e=d
print(max(max(2*e-s-i-k,x-i+j,k-s+x-j)for i,j,k in zip(l,d,d[1:-1])))