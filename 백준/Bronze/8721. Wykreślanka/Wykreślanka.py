n,*l=map(int,open(c:=0).read().split())
for i in l:c+=i==c+1
print(n-c)