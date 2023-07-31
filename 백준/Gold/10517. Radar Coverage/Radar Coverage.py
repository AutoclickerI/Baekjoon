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
for n in range(int(input())):
    a,b,c,d,e,f=map(int,input().split())
    x=a+c+e
    y=b+d+f
    vecs=[vec(a,b),vec(c,d),vec(e,f)]
    point=vec(x/3,y/3)
    lr=LR(0.1,0.999)
    for i in range(20000):
        m=point-vecs[0]
        for j in vecs:
            m=max(m,point-j)
        point=point-lr*m
        lr.step()
    print(f'Case #{n+1}: {point.x:.2f} {point.y:.2f}')