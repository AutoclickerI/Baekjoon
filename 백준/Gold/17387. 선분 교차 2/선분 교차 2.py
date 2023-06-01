ccw=lambda *l:sum(l[i][1]*l[i-1][0]-l[i][0]*l[i-1][1]for i in range(len(l)))/2
def joint(*l):
    x11,y11,x12,y12,x21,y21,x22,y22=l
    p,q=ccw([x11,y11],[x12,y12],[x21,y21])*ccw([x11,y11],[x12,y12],[x22,y22]),ccw([x11,y11],[x21,y21],[x22,y22])*ccw([x12,y12],[x21,y21],[x22,y22])
    if p>0 or q>0:
        return 0
    elif p!=0!=q:
        return 1
    elif p+q:
        return p+q<0
    else:
        a,b=sorted([(x11,y11),(x12,y12)]),sorted([(x21,y21),(x22,y22)])
        return a+b!=sorted(a+b)!=b+a or len(set(a+b))!=4
print(+joint(*map(int,open(0).read().split())))