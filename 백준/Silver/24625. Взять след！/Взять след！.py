n,*l=map(int,open(k:=0))
l=sorted(l)[::-1]
while~k*~k<=n:k+=1
while k>1>l[k-1]:k-=1
print(sum(l[:k]))