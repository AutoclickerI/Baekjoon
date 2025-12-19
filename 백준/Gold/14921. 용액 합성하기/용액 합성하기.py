N,*l=map(int,open(0).read().split())
v=[]
s=0
e=N-1
while s<e:
    x=l[e]+l[s]
    v+=x,
    if 0<x:
        e-=1
    else:
        s+=1
print(min(v,key=abs))