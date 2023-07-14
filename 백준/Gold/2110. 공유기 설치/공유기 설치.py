N,C,*l=map(int,open(0).read().split())
l.sort()
s=1
e=l[-1]+1
def match():
    d=l[0]
    a=1
    for i in l:
        if m<=i-d:
            a+=1
            d=i
    return a>=C
while e-s>1:
    m=(e+s)//2#새 거리
    if match():s=m
    else:e=m
print(s)