def date_abs(m,d):
    return sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:m])+d

l=[]
for i in[*open(0)][1:]:
    a,b,c,d=map(int,i.split())
    v=date_abs(a,b)
    if v<=date_abs(11,30):
        l+=(v,date_abs(c,d)),
d=60
c=m=0
l.sort()
for s,e in l:
    if d<s:
        d=m
        if d<s:
            exit(print(0))
        c+=1
    m=max(e,m)
if date_abs(11,30)<m:
    print(c+(d<=date_abs(11,30)))
else:
    print(0)