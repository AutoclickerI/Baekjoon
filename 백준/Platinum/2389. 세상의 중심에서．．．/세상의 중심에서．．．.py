import sys
input=sys.stdin.readline
class vec:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def size(self):
        return self.x**2+self.y**2
    def __add__(self,b):
        return vec(self.x+b.x,self.y+b.y)
    def __sub__(self,b):
        return vec(self.x-b.x,self.y-b.y)
    def __gt__(self,b):
        return self.size()>b.size()
class LR:
    def __init__(self,init_lr,lr_lambda):
        self.lr=init_lr
        self.lr_lambda=lr_lambda
    def step(self):
        self.lr*=self.lr_lambda
    def __mul__(self,b):
        return vec(self.lr*b.x,self.lr*b.y)
vecs=[]
n=int(input())
x=y=0
for _ in[0]*n:
    p,q=map(float,input().split())
    x+=p
    y+=q
    vecs+=vec(p,q),
point=vec(x/n,y/n)
lr=LR(0.1,0.999)
for i in range(50000):
    m=point-vecs[0]
    for j in vecs:
        m=max(m,point-j)
    point=point-lr*m
    lr.step()
print(point.x,point.y,max((point-i).size()for i in vecs)**.5)