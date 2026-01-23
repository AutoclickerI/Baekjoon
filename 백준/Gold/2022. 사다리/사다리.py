x,y,c=map(eval,input().split())

s=0
e=min(x,y)

for _ in[0]*1000:
    m=(s+e)/2
    if 1<c/(y*y-m*m)**.5+c/(x*x-m*m)**.5:
        e=m
    else:
        s=m
print(s)