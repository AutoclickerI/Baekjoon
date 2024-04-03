rec=[]
for i in[*open(0)][1:]:
    p,q,r,s=map(int,i.split())
    rec+=sorted([r-p,s-q]),

cnt=0
for i in range(len(rec)):
    x1,y1=rec[i]
    for x2,y2 in rec[i+1:]:cnt+=(x1>x2)*(y1<y2)+(x1<x2)*(y1>y2)
print(cnt)