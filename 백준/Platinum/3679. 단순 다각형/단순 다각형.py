def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)

def comp_angle(p1,p2):
    return -ccw(0,0,*p1,*p2)or ((p1[0] or p1[1])>(p2[0] or p2[1]))*2-1

from functools import cmp_to_key

for _ in[0]*int(input()):
    
    _,*l=map(int,input().split())
    *l,=zip(l[::2],l[1::2])
    
    x,y=min(l,key=lambda s:(s[1],s[0]))
    
    l=[(i-x,j-y)for i,j in l]
    d={}
    for i in range(len(l)):
        d[l[i]]=i
    
    l=[i for i in l if i!=(0,0)]
    
    l.sort(key=cmp_to_key(comp_angle))
    
    l=[(0,0),*l]
    
    # Fuck!
    if l[1][0]<0 and ccw(0,0,*l[1],*l[2])==0:
        v=[l[1],l[2]]
        for i in range(3,len(l)):
            if ccw(0,0,*l[1],*l[i])==0:
                v+=l[i],
            else:
                break
        l=[(0,0),*v[::-1],*l[i:]]
    
    v=[]
    # Fuck! 2
    if 0<=l[-1][0]and ccw(0,0,*l[-1],*l[-2])==0:
        v+=l.pop(),
        while ccw(0,0,*v[0],*l[-1])==0:
            v+=l.pop(),
    l+=v
    
    print(*[d[i]for i in l])