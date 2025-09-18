_,K,*l=map(int,open(0).read().split())
t=[0]+[1e9]*K
for i in l:
 for j in range(i,K+1):t[j]=min(t[j],t[j-i]+1)
print(-(1e8<t[K])or t[K])