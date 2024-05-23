_,K,*l=map(int,open(0).read().split())
print(sum(K-i in l for i in l)//2)