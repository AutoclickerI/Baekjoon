[N],*l=[map(int,i.split())for i in open(0)]
p=[0]*1000
for L,R in l:
    for v in*range(L-1),*range(R,1000):
        p[v]+=1
    p=[*map(min,zip([2]+p,p,p[1:]+[2]))]
print(['World Champion','Surrender'][1<min(p)])