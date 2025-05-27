import sys

input=sys.stdin.readline

import math

from decimal import*

def comb_inv_matmul(a,b,c,d,i,j):
    det=a*d-b*c
    return d*i/det-b*j/det

N,h1,h2=map(int,input().split())
p=[(*map(int,input().split()),)for _ in range(N)]

deg=[math.radians(int(input()))for _ in range(N)]

normal=[]

def get_normal(p1,p2,theta):
    (x1,y1),(x2,y2)=p1,p2
    # ax+by+cz=d
    a,b,d=y1-y2,x2-x1,(y1-y2)*x1+(x2-x1)*y1
    c=-(a*a+b*b)**.5/math.tan(theta)
    return(a,b,c),d

for i in range(N):
    normal+=get_normal(p[i],p[(i+1)%N],deg[i]),

#for(a,b,c),d in normal:print(f'{a}x+{b}y+{c}z={d}')

# (i,j,k)v + (p,q)
def line_up_from_plane(n1,n2):
    ((a1,b1,c1),d1),((a2,b2,c2),d2)=n1,n2
    return b1*c2-c1*b2,c1*a2-a1*c2,a1*b2-b1*a2

class link:
    def __init__(self,p,i,prev=None,next=None):
        self.p=p
        self.i=i
        self.prev=prev
        self.next=next

    def __lt__(self,p):
        return self.i<p.i

    def __repr__(self):
        return f'link({self.p},{self.i},{self.prev.i},{self.next.i})'

p_link=[link(p[0],0)]

for i in range(1,N):
    tmp=link(p[i],i)
    tmp.prev=p_link[-1]
    p_link[-1].next=tmp
    p_link+=tmp,

p_link[-1].next=p_link[0]
p_link[0].prev=p_link[-1]

for i in range(N):
    n1,n2=normal[i-1],normal[i]
    p_link[i].lu=line_up_from_plane(n1,n2)

from heapq import heappush,heappop

hq=[]

funcz=funcz2=0

def push(p1,p2):
    (i1,j1,k1),(i2,j2,k2)=p1.lu,p2.lu
    (x1,y1),(x2,y2)=p1.p,p2.p
    theta=deg[p1.i]
    #assert abs(k1*v-k2*w)<1e-6
    h=k1*comb_inv_matmul(i1,-i2,j1,-j2,x2-x1,y2-y1)
    flag=[1]
    p1.flag=flag
    if 0<h:
        heappush(hq,(h,p1,p2,flag))
    a=((x1-x2)**2+(y1-y2)**2)**.5/math.sin(theta)
    return a,a/h

def push_inv(p1,p2):
    (i1,j1,k1),(i2,j2,k2)=p1.lu,p2.lu
    p1.flag[0]=0
    (x1,y1),(x2,y2)=p1.p,p2.p
    theta=deg[p1.i]
    #assert abs(k1*v-k2*w)<1e-6
    h=k1*comb_inv_matmul(i1,-i2,j1,-j2,x2-x1,y2-y1)
    a=((x1-x2)**2+(y1-y2)**2)**.5/math.sin(theta)
    return a,a/h

for i in range(N):
    a,a_h=push(p_link[i],p_link[(i+1)%N])
    funcz+=Decimal(a)
    funcz2-=Decimal(a_h)

def reduce(p1,p2):
    (x1s,y1s),(x1e,y1e),(x2s,y2s),(x2e,y2e)=p1.prev.p,p1.p,p2.p,p2.next.p
    dx1,dy1=x1e-x1s,y1e-y1s
    dx2,dy2=x2e-x2s,y2e-y2s
    t=comb_inv_matmul(dx1,-dx2,dy1,-dy2,x2s-x1s,y2s-y1s)
    nx,ny=x1s+t*dx1,y1s+t*dy1

    p=link((nx,ny),p2.i)

    n1=get_normal(p1.prev.p,p1.p,deg[p1.prev.i])
    n2=get_normal(p2.p,p2.next.p,deg[p2.i])

    p.lu=line_up_from_plane(n1,n2)

    a1,ah1=push_inv(p1.prev,p1)
    a2,ah2=push_inv(p1,p2)
    a3,ah3=push_inv(p2,p2.next)

    p1.prev.next=p2.next.prev=p
    p.prev=p1.prev
    p.next=p2.next

    a4,ah4=push(p.prev,p)
    a5,ah5=push(p,p.next)
    return a4+a5-a1-a2-a3,ah4+ah5-ah1-ah2-ah3

try:
    while hq and hq[0][0]<=h1:
        t=heappop(hq)
        if t[3][0]<1:
            continue
        a,a_h=reduce(t[1],t[2])
        funcz+=Decimal(a)
        funcz2-=Decimal(a_h)

    ans=0
    if not hq:
        print(0)
    else:
        z_cur=h1
        while hq and hq[0][0]<=h2:
            t=heappop(hq)
            if t[3][0]<1:
                continue
            z=t[0]
            ans+=funcz*Decimal(z-z_cur)+funcz2*Decimal(z*z-z_cur**2)/2
            a,a_h=reduce(t[1],t[2])
            funcz+=Decimal(a)
            funcz2-=Decimal(a_h)
            z_cur=z
        ans+=funcz*Decimal(h2-z_cur)+funcz2*Decimal(h2**2-z_cur**2)/2
        print(f'{ans:f}')
except:
    print(0)