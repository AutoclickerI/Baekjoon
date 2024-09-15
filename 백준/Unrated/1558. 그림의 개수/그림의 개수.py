ccw=lambda *l:sum(l[i][1]*l[i-1][0]-l[i][0]*l[i-1][1]for i in range(len(l)))/2
def joint(*l):
    x11,y11,x12,y12,x21,y21,x22,y22=l
    p,q=ccw([x11,y11],[x12,y12],[x21,y21])*ccw([x11,y11],[x12,y12],[x22,y22]),ccw([x11,y11],[x21,y21],[x22,y22])*ccw([x12,y12],[x21,y21],[x22,y22])
    if p>0 or q>0:
        return 0
    elif p!=0!=q:
        return 1
    elif p+q:
        return (p+q<0)*3
    else:
        a,b=sorted([(x11,y11),(x12,y12)]),sorted([(x21,y21),(x22,y22)])
        return (a+b!=sorted(a+b)!=b+a or len(set(a+b))!=4)*2
    
def cross(x1,y1,x2,y2,x3,y3,x4,y4):
    (x1,y1),(x2,y2)=sorted([(x1,y1),(x2,y2)])
    (x3,y3),(x4,y4)=sorted([(x3,y3),(x4,y4)])
    if (x1,y1)==(x2,y2):
        if (x1,y1) in [(x3,y3),(x4,y4)]:
            return 1
        dx1,dx2=x1-x3,x4-x1
        dy1,dy2=y1-y3,y4-y1
        if dx1==0:
            return dx2==0 and y3<y1<y4
        if x3<x1<x4:
            return dx2*dy1==dx1*dy2
        return 0
    if (x3,y3)==(x4,y4):
        if (x3,y3) in [(x1,y1),(x2,y2)]:
            return 1
        dx1,dx2=x3-x1,x2-x3
        dy1,dy2=y3-y1,y2-y3
        if dx1==0:
            return dx2==0 and y1<y3<y2
        if x1<x3<x2:
            return dx2*dy1==dx1*dy2
        return 0
    n=joint(x1,y1,x2,y2,x3,y3,x4,y4)
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n==3:
        return 1
    else:
        return 0

N=int(input())
p=[]
for _ in[0]*N:
    tmp=[]
    for _ in[0]*int(input()):
        tmp+=tuple(map(int,input().split())),
    if len(tmp)==1:
        tmp*=2
    p+=[],
    for i,j in zip(tmp,tmp[1:]):
        p[-1]+=(*i,*j),

def check(l1,l2):
    for i in l1:
        for j in l2:
            if cross(*i,*j):
                return 1
    return 0

d={0:p[0]}
for idx in range(N):
    init=-1
    for i in*d,:
        if check(p[idx],d[i]):
            if init<0:
                init=i
                d[i]+=p[idx]
            else:
                d[init]+=d[i]
                del d[i]
    if init<0:
        d[idx]=p[idx]
print(len(d))