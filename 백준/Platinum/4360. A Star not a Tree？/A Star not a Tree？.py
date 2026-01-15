import sys
input=sys.stdin.readline

class vec:
    def __init__(self,p):
        self.p=p
    def size(self):
        return sum(i*i for i in self.p)
    def __add__(self,b):
        return vec([i+j for i,j in zip(self.p,b.p)])
    def __sub__(self,b):
        return vec([i-j for i,j in zip(self.p,b.p)])
    def __mul__(self,m):
        return vec([i*m for i in self.p])
    def __truediv__(self,m):
        return vec([i/m for i in self.p])
    def __gt__(self,b):
        return self.size()>b.size()
class LR:
    def __init__(self,init_lr,lr_lambda):
        self.lr=init_lr
        self.lr_lambda=lr_lambda
    def step(self):
        self.lr*=self.lr_lambda
    def __mul__(self,b):
        return vec([self.lr*i for i in b.p])
vecs=[]
n=int(input())
x=y=0
for _ in[0]*n:
    p,q=map(int,input().split())
    x+=p
    y+=q
    vecs+=vec([p,q]),
point=vec([x/n,y/n])
lr=LR(10000,0.999)
for i in range(50000):
    m=vec([0,0])
    for j in vecs:
        d=point-j
        if 1e-12<d.size():
            m+=d/d.size()**.5
    point=point-lr*m
    lr.step()
print(round(sum((i-point).size()**.5 for i in vecs)))