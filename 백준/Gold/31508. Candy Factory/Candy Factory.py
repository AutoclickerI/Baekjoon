N,K,*A=map(int,open(0).read().split())
s=sum(A)
print(max(0-s//-K,*A)*K-s)