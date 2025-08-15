z=[0]*5**6
for i in open(0):
    p,q,r,s=map(int,i.split())
    for y in range(p,r):z[y<<7|q:y<<7|s]=[1]*(s-q)
print(sum(z))