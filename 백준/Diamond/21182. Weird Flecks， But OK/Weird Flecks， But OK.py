import sys
input=sys.stdin.readline
class vec:
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
    def size(self):
        return self.x**2+self.y**2+self.z**2
    def __add__(self,b):
        return vec(self.x+b.x,self.y+b.y,self.z+b.z)
    def __sub__(self,b):
        return vec(self.x-b.x,self.y-b.y,self.z-b.z)
    def __gt__(self,b):
        return self.size()>b.size()
class LR:
    def __init__(self,init_lr,lr_lambda):
        self.lr=init_lr
        self.lr_lambda=lr_lambda
    def step(self):
        self.lr*=self.lr_lambda
    def __mul__(self,b):
        return vec(self.lr*b.x,self.lr*b.y,self.lr*b.z)
n=int(input())
vecxy=[]
vecyz=[]
veczx=[]
x=y=z=0
for _ in[0]*n:
    p,q,r=map(float,input().split())
    x+=p
    y+=q
    z+=r
    vecxy+=vec(p,q),
    vecyz+=vec(q,r),
    veczx+=vec(r,p),
pointxy=vec(x/n,y/n)
pointyz=vec(y/n,z/n)
pointzx=vec(z/n,x/n)
lr=LR(0.1,0.999)
for i in range(20000):
    mxy=pointxy-vecxy[0]
    myz=pointyz-vecyz[0]
    mzx=pointzx-veczx[0]
    for j in vecxy:
        mxy=max(mxy,pointxy-j)
    for j in vecyz:
        myz=max(myz,pointyz-j)
    for j in veczx:
        mzx=max(mzx,pointzx-j)
    pointxy=pointxy-lr*mxy
    pointyz=pointyz-lr*myz
    pointzx=pointzx-lr*mzx
    lr.step()
print(2*min(max((pointxy-i).size()for i in vecxy),max((pointyz-i).size()for i in vecyz),max((pointzx-i).size()for i in veczx))**.5)