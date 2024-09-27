(n,m),*l=[map(int,i.split())for i in open(0)]
for d,g in sorted((b-a,a)for a,b in zip(*l)):m+=g*(d<=m)
print(m)