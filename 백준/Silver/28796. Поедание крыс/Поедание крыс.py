n,k,*l=map(int,open(a:=0).read().split())
l=l[::-1]
while l and a+l[-1]<=k:a+=l.pop()
print(a)