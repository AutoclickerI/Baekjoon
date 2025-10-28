[n,C],*l=[map(int,i.split())for i in open(0)]
v=sorted([*zip(*l[:n])][0])
for t,k in l[n+1:]:print((v[k-1]**2+2*C*t)**.5)