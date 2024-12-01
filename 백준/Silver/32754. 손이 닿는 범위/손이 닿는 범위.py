N,R=map(int,input().split())
a=0
for _ in[0]*N:
    x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    x,y=(x1+x2+x3+x4)/4,(y1+y2+y3+y4)/4
    if (x*x+y*y)**.5-((x-x1)**2+(y-y1)**2)**.5<=R:
        a+=1
print(a)