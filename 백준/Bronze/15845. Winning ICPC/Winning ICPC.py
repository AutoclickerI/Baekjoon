n,t,*l=[[*map(int,i.split())]for i in open(0)]
print(min((-sum(i==j for i,j in zip(l[k],t)),k)for k in range(n[0]))[1]+1)