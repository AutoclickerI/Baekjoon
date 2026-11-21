_,M,K,*l=map(int,open(o:=0).read().split())
for i in range(M):K>=(o:=o+l[2*i+1])or exit(print(i+1,1))
print(-1)