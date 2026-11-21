N,K,*l=map(int,open(0).read().split())
print(sum(sorted(l)[-K:])-~-K*K//2)