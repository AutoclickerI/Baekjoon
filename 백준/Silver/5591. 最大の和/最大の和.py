a,b,*l=map(int,open(0).read().split())
t=m=sum(l[:b])
for i in range(b,a):t+=l[i]-l[i-b];m=max(t,m)
print(m)