_,K,*l=open(r:=0).read().split()
L=[0]*22
K=int(K)
for i,x in enumerate(l):L[len(l[i+~K])]-=K<i;r+=L[x:=len(x)];L[x]+=1
print(r)