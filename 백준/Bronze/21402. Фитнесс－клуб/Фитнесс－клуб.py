(n,k),*l=[map(int,i.split())for i in open(0)]
c=k
for a,b in l:c=min(c+a,k-b)
print(c)