n,a,b,T=open(0)
n,N=map(int,n.split())
for _,_,c in sorted((i+int(T)*(i<n),-i,(a[::-1]+b)[i+1])for i in range(n+N)):print(end=c)