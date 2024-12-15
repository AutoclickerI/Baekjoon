class circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def __call__(self,x,y):
        return(self.y-y)**2+(self.x-x)**2<=self.r**2

class rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def __call__(self,x,y):
        return self.x1<=x<=self.x2 and self.y1<=y<=self.y2

d=[]
for _ in[0]*int(input()):
    f,*l=input().split()
    d+=eval(f"{f}({','.join(l)})"),

for _ in[0]*int(input()):
    *v,=map(int,input().split())
    print(sum(i(*v)for i in d))