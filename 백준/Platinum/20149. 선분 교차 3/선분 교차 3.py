from decimal import*
getcontext().prec=199
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
x1,y1,x2,y2,x3,y3,x4,y4=map(int,open(0).read().split())
n=joint(x1,y1,x2,y2,x3,y3,x4,y4)
p,q,r,s=ccw([x1,y1],[x2,y2],[x3,y3]),ccw([x1,y1],[x2,y2],[x4,y4]),ccw([x1,y1],[x3,y3],[x4,y4]),ccw([x2,y2],[x3,y3],[x4,y4])
if n==1:
    Z=Decimal('1E-100');x2+=Z;y2+=Z;x4+=Z*2;y4+=Z
    k1=(y2-y1)/(x2-x1)
    k2=x1*(y2-y1)/(x2-x1)-y1
    k3=(y4-y3)/(x4-x3)
    k4=x3*(y4-y3)/(x4-x3)-y3
    print(1)
    x=(k4-k2)/(k3-k1)
    print(f'{x:.10f} {x*k1-k2:.10f}')
elif n==2:
    a,b=sorted([(x1,y1),(x2,y2)]),sorted([(x3,y3),(x4,y4)])
    print(1)
    if a+b==sorted(a+b) or b+a==sorted(a+b) or ((p or q)and(r or s)):
        for i in a:
            if i in b:
                print(*i)
elif n==3:
    print(1)
    if p*q==0:
        if p:
            print(x4,y4)
        else:
            print(x3,y3)
    else:
        if r:
            print(x2,y2)
        else:
            print(x1,y1)
else:
    print(0)