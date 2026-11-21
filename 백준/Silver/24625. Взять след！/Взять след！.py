n,*l=map(int,open(k:=0))
l.sort()
while~k*~k<=n:k+=1
while k>1>l[-k]:k-=1
print(sum(l[-k:]))