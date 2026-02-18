import math

for i in[*open(0)][1:]:
    x1,y1,x2,y2=map(int,i.split())
    x1,y1,x2,y2=0,min(y1,y2),abs(x2-x1),max(y1,y2)
    if x2-x1<1:
        print(math.log(y2)-math.log(y1))
    else:
        xM,yM=x2/2,(y1+y2)/2
        C=xM+yM*(y2-y1)/x2
        t1=math.atan2(y1,C)
        t2=math.atan2(y2,C-x2)
        print(math.log(abs(1/math.sin(t2)-1/math.tan(t2)))-math.log(abs(1/math.sin(t1)-1/math.tan(t1))))