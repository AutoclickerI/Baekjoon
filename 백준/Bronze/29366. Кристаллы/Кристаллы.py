_,a,b=[map(int,i.split())for i in open(0)]
*l,=map(int.__sub__,a,b)
if max(l)<0 or 0<min(l):
    print(-1)
else:
    mi=l.index(min(l))+1
    Mi=l.index(max(l))+1
    cm=max(l)
    cM=-min(l)
    print(cm+cM)
    print(*[mi]*cm+[Mi]*cM)