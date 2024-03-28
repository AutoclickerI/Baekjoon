p,q=map(str.split,open(0))
*l,=map(int,p)
*L,=map(int,q)
s=sum(l)
S=sum(L)
if s>S:print('Algosia')
elif s<S:print('Bajtek')
else:
    for i in range(10,0,-1):
        if l.count(i)>L.count(i):
            print('Algosia');break
        if l.count(i)<L.count(i):
            print('Bajtek');break
    else:print('remis')