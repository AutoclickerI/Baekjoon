N,*l=map(int,open(0).read().split())
N=1
t=[1]
d=[]
for i in l[:-1][::-1]:
    N+=1
    if i==1:
        t+=N,
    if i==2:
        t+=N,t.pop()
    if i==3:
        d+=N,
print(*t[::-1],*d)