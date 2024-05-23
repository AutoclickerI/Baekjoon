_,K,*l=map(int,open(0).read().split())
print(len({K-i for i in l}&{*l})//2)