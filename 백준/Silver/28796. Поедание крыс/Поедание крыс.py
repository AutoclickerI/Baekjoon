n,k,*l=map(int,open(a:=0).read().split())
while a+l[-n]<=k:a+=l[-n];n-=1
print(a)