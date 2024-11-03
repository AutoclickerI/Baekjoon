from bisect import bisect_left
n,t=map(int,input().split())
class line:
    def __init__(self,xs,ys,xe,ye,dir=1,idx=0):
        self.xs=xs
        self.ys=ys
        self.xe=xe
        self.ye=ye
        self.vert=xs==xe
        self.intersect=[(ys if self.vert else xs,self)]
        self.dir=dir
        self.idx=idx
    def cross(self,l2):
        if self.vert^l2.vert:
            if self.vert and self.ys<l2.ys<self.ye and l2.xs<self.xs<l2.xe:
                self.intersect+=(l2.ys,l2),
                l2.intersect+=(self.xs,self),
            elif l2.vert and self.xs<l2.xs<self.xe and l2.ys<self.ys<l2.ye:
                self.intersect+=(l2.xs,l2),
                l2.intersect+=(self.ys,self),
    def getnext(self):
        if self.dir==1 and self.idx==len(self.intersect)-1:
            self.dir=-1
        elif self.dir==-1 and self.idx==0:
            self.dir=1
        tmp=self.idx+self.dir
        val=abs(self.intersect[tmp][0]-self.intersect[self.idx][0])
        self.idx=tmp
        return val,self.intersect[tmp][1]
    def set_idx_dir(self,n,d,v):
        self.idx=bisect_left(self.intersect,(n,))
        self.dir=d*(1-2*v)
    def __repr__(self):
        return f'line({self.xs},{self.ys},{self.xe},{self.ye},{self.dir},{self.idx})'

flag=True
lines=[]
for _ in[0]*n:
    xs,ys,xe,ye=map(int,input().split())
    if flag:
        x1,y1=xs,ys
        flag=False
    (xs,ys),(xe,ye)=sorted([(xs,ys),(xe,ye)])
    lines+=line(xs,ys,xe,ye),
for i in range(n):
    for j in lines[i+1:]:
        lines[i].cross(j)

for i in lines:
    i.intersect+=(i.ye if i.vert else i.xe,i),
    i.intersect.sort()

ans=0
line_cur=lines[0]
while True:
    val,line_next=line_cur.getnext()
    ans+=val
    if line_cur.idx not in[0,len(line_cur.intersect)-1]:
        line_next.set_idx_dir(line_cur.xs if line_cur.vert else line_cur.ys,line_cur.dir,line_cur.vert)
    line_cur=line_next
    if line_cur==lines[0]and (line_cur.dir,line_cur.idx)==(-1,0):
        break
t%=ans

if(lines[0].xs,lines[0].ys)==(x1,y1):
    lines[0].dir=1
    lines[0].idx=0
else:
    lines[0].dir=-1
    lines[0].idx=len(lines[0].intersect)-1

while True:
    val,line_next=line_cur.getnext()
    t-=val
    if t<=0:
        break
    if line_cur.idx not in[0,len(line_cur.intersect)-1]:
        line_next.set_idx_dir(line_cur.xs if line_cur.vert else line_cur.ys,line_cur.dir,line_cur.vert)
    line_cur=line_next

if line_cur.vert:
    print(line_cur.xs,line_cur.intersect[line_cur.idx][0]+t*line_cur.dir)
else:
    print(line_cur.intersect[line_cur.idx][0]+t*line_cur.dir,line_cur.ys)