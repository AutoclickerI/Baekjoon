[N,L],*l=[[*map(int,i.split())]for i in open(0)]
l.sort()
r=0
el=0
for s,e in l:
    s=max(el,s)
    x=(s-e)//L
    el=s+x*-L
    r-=x
print(r)