_,W,*s=map(int,open(0).read().split())
for i,j in zip(s,s[1:]):W=max(W,W%i+W//i*j)
print(W)