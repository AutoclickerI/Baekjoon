from itertools import combinations
from collections import Counter
def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


def is_two_lines_intersecting(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    mx1, my1 = min(x1, x2), min(y1, y2)
    mx2, my2 = max(x1, x2), max(y1, y2)
    mx3, my3 = min(x3, x4), min(y3, y4)
    mx4, my4 = max(x3, x4), max(y3, y4)

    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True
    else:
        if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
            return True

    return False

n=int(input())
L=[]
for P,Q in combinations([[i,*map(int,input().split())]for i in range(n)],2):
    if is_two_lines_intersecting(P[1:],Q[1:]):
        L+=[[P[0],Q[0]]]
P=[*range(n)]
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
for i in L:
 a,b=sorted(map(F,i))
 if a-b:P[b]=a
for i in range(n):
    P[i]=F(P[i])
lis=Counter(P).most_common()
print(len(lis),lis[0][1])