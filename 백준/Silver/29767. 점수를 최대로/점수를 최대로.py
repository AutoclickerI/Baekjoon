N,K,*l=map(int,open(s:=0).read().split())
print(sum(sorted(s:=s+i for i in l)[-K:]))