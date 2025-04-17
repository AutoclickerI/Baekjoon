n,k,*l=map(int,open(0).read().split())
t,s=k,1
for i in l:t,s=[t,k][f:=t<i]-i,s+f
print(s)