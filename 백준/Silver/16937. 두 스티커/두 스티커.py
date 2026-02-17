[H,W],_,*l=[[*map(int,i.split())]for i in open(0)]
from itertools import*

m=0
for(R1,C1),(R2,C2)in combinations(l,2):
    ps=[(max(r1,r2),c1+c2)for r1,c1 in[(R1,C1),(C1,R1)]for r2,c2 in[(R2,C2),(C2,R2)]]
    for R,C in ps:
        if R<=H and C<=W or C<=H and R<=W:
            m=max(m,R1*C1+R2*C2)
print(m)