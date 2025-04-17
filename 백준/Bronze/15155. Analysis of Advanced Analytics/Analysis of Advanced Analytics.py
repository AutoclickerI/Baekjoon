n,k,*l=map(int,open(0).read().split())
t,s=k,1
for i in l:f=t<i;t,s=[t,k][f]-i,s+f
print(s)