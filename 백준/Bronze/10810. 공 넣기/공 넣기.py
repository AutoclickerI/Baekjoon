p,*l=open(0)
L=[0]*int(p.split()[0])
for i in l:
 p,q,r=map(int,i.split())
 for j in range(p-1,q):L[j]=r
print(*L)