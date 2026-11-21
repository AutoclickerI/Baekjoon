from itertools import combinations
import math
N=int(input())
l=[[i,*map(int,input().split())]for i in range(N)]
node=[]
for p,q in combinations(l,2):
    a,b,c,r1=p
    d,e,f,r2=q
    distpow=((e-b)**2+(c-f)**2)
    if distpow<=(r1+r2)**2:
        price=0
    else:
        price=2*(distpow-(r1-r2)**2)**.5
        theta1=math.acos((r1-r2)/distpow**.5)
        price+=r1*2*(math.pi-theta1)
        price+=r2*2*theta1
    node+=[[a,d,price]]
q=N*(N+1)//2
P=[*range(N)]
A=0
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
S=sorted
for a,b,c in S(node,key=lambda l:l[2]):
 a,b=S([F(a),F(b)])
 if a-b:A+=c;P[b]=a
print(A)