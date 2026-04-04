l=[[*map(int,i.split())]for i in open(0)][1:]

x,y=min(l,key=lambda s:(s[1],s[0]))

l=[(i-x,j-y)for i,j in l]

def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)

def comp_angle(p1,p2):
    return -ccw(0,0,*p1,*p2)or (abs(p1[0]+p1[1])>abs(p2[0]+p2[1]))*2-1

from functools import cmp_to_key

l.sort(key=cmp_to_key(comp_angle))

ch=[]

for i in l:
    while 1<len(ch) and ccw(*ch[-2],*ch[-1],*i)<=0:
        ch.pop()
    ch+=i,

def dist(a,b):
    return((a[0]-b[0])**2+(a[1]-b[1])**2)**.5

ch*=2
r=0
s=e=0
while s<e+1<len(ch):
    r=max(r,dist(ch[s],ch[e]))
    if dist(ch[s],ch[e])<dist(ch[s],ch[e+1]):
        e+=1
    else:
        s+=1
print(r)