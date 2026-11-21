(n,k),*x=[map(int,i.split())for i in open(0)]
l=[0]*6
for a,b in x:l[~-b//2*2+a*(b>2)]+=1
print(-sum(i//-k for i in l))