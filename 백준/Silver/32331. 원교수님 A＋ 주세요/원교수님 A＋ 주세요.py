N,M,X,Y=map(int,input().split())
_,s=map(int,input().split())
l=[]
for _ in[0]*~-N:
    x,t=map(int,input().split())
    x//=1000000
    if x==2024:
        l+=t+max(t+Y-X,0),
l.sort()
try:
    t=l[-M]-s
    if t>Y:
        print('NO')
    else:
        print('YES')
        print(max(t,0))
except:
    print('YES')
    print(0)