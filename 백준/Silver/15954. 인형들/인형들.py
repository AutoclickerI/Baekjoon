n,k,*l=map(int,open(0).read().split())
r=[]
for j in range(k,n+1):
 for i in range(n-j+1):m=sum(p:=l[i:i+j])/j;r+=sum((v-m)**2for v in p)/j,
print(min(r)**.5)