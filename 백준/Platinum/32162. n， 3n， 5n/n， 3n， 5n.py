l=[1]
s={1}
i=1
while len(l)<100000:
    i+=1
    if i%3<1 or i%5<1:
        x=i
        t=f=0
        while x%3<1:
            x//=3;t+=1
        while x%5<1:
            x//=5;f+=1
        m=min(t,f)
        t-=m;f-=m
        if not (x%5>0<x%3 and t%3<1>f%3):
            continue
    l+=i,
    s.add(i)

for i in[*open(0)][1:]:print(l[int(i)-1])