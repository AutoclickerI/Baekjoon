p,q=input().split()
l=min(len(p),len(q))
print(p[:-l]+q[:-l],*[int(i)+int(j)for i,j in zip(p[-l:],q[-l:])],sep='')