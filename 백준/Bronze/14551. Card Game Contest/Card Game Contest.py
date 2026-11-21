_,M,*l=map(int,open(0).read().split())
S=1
for i in l:S=S*max(i,1)
print(S%M)