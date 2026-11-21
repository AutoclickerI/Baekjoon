N,K,T,*l=map(int,open(t:=0).read().split())
for i,j in zip(l,l[N:]):t+=i;t=[max(t,j)+T,t+K][t+K<j]
print(t)