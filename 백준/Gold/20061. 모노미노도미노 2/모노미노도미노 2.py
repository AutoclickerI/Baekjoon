a=[0]

class box:
    def __init__(self):
        self.b=[4*[0]for _ in[0]*10]
    def drop(self,arr):
        offset=0
        while max(arr)[0]+offset<9 and sum(self.b[y+offset+1][x]for y,x in arr)<1:
            #print(max(arr)[0]+offset,offset)
            offset+=1
        for y,x in arr:
            self.b[y+offset][x]=1
        b=[]
        for i in self.b:
            if sum(i)==4:
                a[0]+=1
            elif sum(i):
                b+=i,
        self.b=([4*[0]for _ in[0]*10]+b[:4])[-10:]

box1=box()
box2=box()

for i in[*open(0)][1:]:
    t,x,y=map(int,i.split())
    if t==1:
        box1.drop([(x,y)])
        box2.drop([(y,x)])
    if t==2:
        box1.drop([(x,y),(x,y+1)])
        box2.drop([(y,x),(y+1,x)])
    if t==3:
        box1.drop([(x,y),(x+1,y)])
        box2.drop([(y,x),(y,x+1)])
print(*a)
print(sum(sum(i)for i in box1.b+box2.b))