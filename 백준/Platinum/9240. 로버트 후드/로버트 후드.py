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
    return(a[0]-b[0])**2+(a[1]-b[1])**2

ch*=2
r=0
p1=0
p2=1
while p1<p2+1<len(ch):
    A,B=ch[p1],ch[p1+1]
    C,D=ch[p2],ch[p2+1]
    AB=B[0]-A[0],B[1]-A[1]
    CD=D[0]-C[0],D[1]-C[1]
    r=max(r,dist(A,C))
    if ccw(0,0,*AB,*CD)<0:
        p1+=1
    else:
        p2+=1
print(r**.5)