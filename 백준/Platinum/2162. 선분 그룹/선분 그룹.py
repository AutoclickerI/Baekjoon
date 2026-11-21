from itertools import combinations
from collections import Counter

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

n=int(input())
L=[]
for P,Q in combinations([[i,*map(int,input().split())]for i in range(n)],2):
    if joint(*P[1:],*Q[1:]):
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