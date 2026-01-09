n,*l=map(int,open(0).read().split())
d=[0]*n
for i in range(n):v=d[i]=max(d[j-1]+abs(l[i]-l[j])for j in range(i+1))
print(v)