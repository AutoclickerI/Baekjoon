_,l,*b=zip(*sorted([sorted(map(int,i.split()))for i in open(0)][1:]))
from bisect import*
for v in l:i=bisect(b,v);b[i:i+1]=v,
print(len(b))