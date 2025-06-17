o=[]
e=[]
c=[]
for i in map(int,[*open(0)][1].split()):
    if i%2:
        o+=i,
    else:
        e+=i,
    if c and c[-1][0]+i&1<1:
        c[-1]+=i,
    else:
        c+=[i],

if o==sorted(o)and e==sorted(e):
    print('So Lucky')
else:
    print('Unlucky')

for i in c:i.sort()

z=sum(c,[])

if z==sorted(z):
    print('So Lucky')
else:
    print('Unlucky')