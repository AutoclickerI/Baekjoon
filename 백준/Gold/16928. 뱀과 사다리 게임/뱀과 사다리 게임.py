from collections import deque
p,q=map(int,input().split())
d={}
for _ in[0]*(p+q):
    p,q=map(int,input().split())
    d[p]=q
v=[1]*200
Q=deque([(i:=1,0)])
while i-100:
    i,j=Q.popleft()
    if i in d:
        if v[d[i]]:Q.append((d[i],j));v[d[i]]=0
    else:
        for k in range(6):
            if i+1+k in d:
                if v[d[i+1+k]]:Q.append((d[i+1+k],j+1));v[d[i+1+k]]=0
            elif v[i+1+k]:v[i+1+k]=0;Q.append((i+1+k,j+1))
print(j)