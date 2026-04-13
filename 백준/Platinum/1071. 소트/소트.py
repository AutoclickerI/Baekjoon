N,*l=map(int,open(0).read().split())
d={}
for i in l:
    d[i]=d.get(i,0)+1
sl=sorted(d)

r=[]

while sl:
    if len(sl)<2:
        r+=sl*d[sl[0]]
        break
    if len(sl)==2 and sl[0]+1==sl[1]:
        for i in sl[::-1]:
            r+=[i]*d[i]
        break
    if sl[0]+1==sl[1]:
        r+=*[sl[0]]*d[sl[0]],sl[2]
        d[sl[2]]-=1
        if d[sl[2]]<1:
            sl.pop(2)
        sl.pop(0)
    else:
        i=sl.pop(0)
        r+=[i]*d[i]
print(*r)