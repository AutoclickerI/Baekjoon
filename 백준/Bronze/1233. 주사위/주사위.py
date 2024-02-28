p,q,r=map(int,input().split())
d={}
for i in range(p):
    for j in range(q):
        for k in range(r):
            d[i+j+k+3]=d.get(i+j+k+3,0)+1
print(min(i for i in d if d[i]==max(d.values())))