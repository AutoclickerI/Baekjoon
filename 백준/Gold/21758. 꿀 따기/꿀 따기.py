s,*l,e=map(int,[*open(0)][1].split())
r1=sum(l)+max(l)
r2m=r2=(sum(l)+e-l[0])*2
for i,j in zip(l,l[1:]+[e]):
    r2+=i-2*j
    r2m=max(r2m,r2)
s,e=e,s
l=l[::-1]
r3m=r3=(sum(l)+e-l[0])*2
for i,j in zip(l,l[1:]+[e]):
    r3+=i-2*j
    r3m=max(r3m,r3)
print(max(r1,r2m,r3m))