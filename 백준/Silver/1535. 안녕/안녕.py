[N],L,J=[[*map(int,i.split())]for i in open(0)]
m=0
for i in range(2**N):
 c=v=j=0
 while i:c+=i%2*L[v];j+=i%2*J[v];i//=2;v+=1
 m=max(j*(c<100),m)
print(m)