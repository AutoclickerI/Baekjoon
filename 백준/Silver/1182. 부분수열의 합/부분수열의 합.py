p,q=open(0)
l=[0]
for j in q.split():l+=[i+int(j)for i in l]
print(l[1:].count(int(p[2:])))