from bisect import bisect_left
def collect(pos):
    global ans
    idx=bisect_left(db,pos)
    if len(db)==idx or idx>0 and pos-db[idx-1]<=db[idx]-pos:
        idx-=1
    s=e=idx
    while e-s<len(db):
        ans+=abs(pos-db[idx])
        pos=db[idx]
        if e>=len(db)-1 or 0<s and pos-db[s-1]<=db[e+1]-pos:
            s-=1
            idx=s
        else:
            e+=1
            idx=e
    return pos
        
db=[]
p=0
ans=0
for _ in[0]*int(input()):
    q,*l=map(int,input().split())
    db+=l
    if q==2:
        db.sort()
        p=collect(p)
        db=[]
print(ans)