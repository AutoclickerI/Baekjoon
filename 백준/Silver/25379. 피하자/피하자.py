*l,=map(int,[*open(0)][1].split())
v=c=r=0
for i in l:
    if i%2==c:
        r+=1
    else:
        v+=r
v2=r=0
c=1
for i in l:
    if i%2==c:
        r+=1
    else:
        v2+=r
print(min(v,v2))