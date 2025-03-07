import math
from fractions import*

class vec:
    def __init__(self,l,k=None):
        self.k=k
        if not k:
            self.k=math.gcd(*l)
        self.l=tuple([i//self.k for i in l])

n=int(input())
board=[[*map(int,input().split())]for _ in[0]*n]

x=[vec(i)for i in board]
y=[vec(i)for i in zip(*board)]

if len({i.l for i in x})>1 or len({i.l for i in y})>1:
    print(-1)
else:
    d={}
    x={i.k for i in x}
    y={i.k for i in y}
    for i in x:
        for j in y:
            f=Fraction(i,j)
            d[f]=d.get(f,0)+1
    print(len(x)+len(y)-max(d.values()))