n,*l=map(int,open(0).read().split())
l.sort()
print(m:=sum(l[:n//2]),sum(l)-m)