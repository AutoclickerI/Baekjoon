def check(x1,y1,p1,q1,x2,y2,p2,q2):
    (x1,y1,p1,q1),(x2,y2,p2,q2)=sorted([(x1,y1,p1,q1),(x2,y2,p2,q2)])
    if q1<y2 or q2<y1 or p1<x2:
        return 'd'
    if (p1,q1)==(x2,y2) or (p1,y1)==(x2,q2):
        return 'c'
    if q1==y2 or q2==y1 or p1==x2:
        return 'b'
    return 'a'
for i in open(0):print(check(*map(int,i.split())))