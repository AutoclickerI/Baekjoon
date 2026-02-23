*z,=zip(*[map(int,i.split())for i in open(0)][1:])
l=[]
for i in z:
    m=max(i)
    if i.count(m)==1:
        l+=i.index(m),
print(len({*l}))