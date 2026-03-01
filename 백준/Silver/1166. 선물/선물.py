N,L,W,H=map(int,input().split())

s=0
e=10**99

for _ in[0]*1000:
    m=(s+e)/2
    if(L//m)*(W//m)*(H//m)<N:
        e=m
    else:
        s=m
print(s)