l=open(0).read().split()[1:]
l2=sorted([(i.replace(*'kc').replace(*'pq').replace(*'op').replace('ng','o'),i)for i in l])
for i,j in l2:print(j)