n,*l=map(int,open(0).read().split())
print(max(-~n//2-sum(i<2for i in l),0))