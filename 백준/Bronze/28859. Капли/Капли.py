n,k,t,*l=map(int,open(0).read().split())
print(sum(t//k*(k//i)+t%k//i for i in l))