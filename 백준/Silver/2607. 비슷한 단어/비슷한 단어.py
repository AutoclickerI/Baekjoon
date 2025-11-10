def cnt(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    return d

_,s,*l=open(0)
v=cnt(s)
a=0

for i in l:
    x=cnt(i)
    q=[]
    for c in{*v,*x}:
        if v.get(c,0)-x.get(c,0):
            q+=v.get(c,0)-x.get(c,0),
    a+=q in([],[1],[-1],[-1,1],[1,-1])
print(a)