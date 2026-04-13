import sys
input=sys.stdin.readline

from functools import cmp_to_key

def ccw(x1,y1,x2,y2,x3,y3):
    return (x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)

def comp_angle(p1,p2):
    c1=-ccw(0,0,*p1,*p2)
    if c1:
        return c1
    
    return (p1[0]**2+p1[1]**2>p2[0]**2+p2[1]**2)*2-1

def dist(a,b):
    return(a[0]-b[0])**2+(a[1]-b[1])**2

for T in range(int(input())):
    l=[[*map(int,input().split())]for i in[0]*int(input())]
    
    x,y=min(l,key=lambda s:(s[1],s[0]))
    
    l=[(i-x,j-y)for i,j in l]
    
    l.sort(key=cmp_to_key(comp_angle))
    
    ch=[]
    
    for i in l:
        while 1<len(ch) and ccw(*ch[-2],*ch[-1],*i)<=0:
            ch.pop()
        ch+=i,
    
    ch*=2
    r=0
    p1=0
    p2=1
    while p1<p2+1<len(ch):
        A,B=ch[p1],ch[p1+1]
        C,D=ch[p2],ch[p2+1]
        AB=B[0]-A[0],B[1]-A[1]
        CD=D[0]-C[0],D[1]-C[1]
        nr=dist(A,C)
        if r<nr:
            r=nr
            a=A[0]+x,A[1]+y,C[0]+x,C[1]+y
        if ccw(0,0,*AB,*CD)<0:
            p1+=1
        else:
            p2+=1
    print(*a)