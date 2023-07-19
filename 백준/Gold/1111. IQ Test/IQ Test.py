n=int(input())
*l,=map(int,input().split())
s=set()
if len(l)==1:
    exit(print('A'))
for a in range(-100000,100000):
    b=l[1]-a*l[0]
    for n,m in zip(l,l[1:]):
        if a*n+b!=m:
            break
    else:
        s.add(l[-1]*a+b)
if len(s)>1:
    print('A')
elif s:
    print(next(iter(s)))
else:
    print('B')