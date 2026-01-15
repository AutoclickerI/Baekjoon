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
n=3
x=y=z=0
for _ in[0]*n:
    p,q,r=map(int,input().split())
    x+=p
    y+=q
    z+=r
    vecs+=vec([p,q,r]),
point=vec([x/n,y/n,z/n])
lr=LR(10**10,0.999)
for i in range(50000):
    m=vec([0,0,0])
    for j in vecs:
        d=point-j
        if d.size()**.5:
            m-=d/d.size()**.5
    point=point+lr*m
    lr.step()
print(sum((i-point).size()**.5 for i in vecs))