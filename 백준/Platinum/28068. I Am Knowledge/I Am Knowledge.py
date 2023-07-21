asc=[]
desc=[]
for i in[*open(0)][1:]:
    p,q=map(int,i.split())
    if q<p:desc+=(q,p),
    else:asc+=(p,q),    
asc.sort()
desc.sort()
e=0
for i,j in asc:
    e-=i
    if e<0:exit(print(0))
    e+=j
for j,i in desc[::-1]:
    e-=i
    if e<0:exit(print(0))
    e+=j
print(1)