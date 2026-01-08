N=int(input())

s=-1
e=2**32

while 1<e-s:
    m=(s+e)//2
    if N<=m*m:
        e=m
    else:
        s=m
print(e)