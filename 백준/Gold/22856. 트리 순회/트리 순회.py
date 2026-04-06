[N],*l=[[*map(int,i.split())]for i in open(0)]
l=[0]+sorted(l)

e=1
while l[e][2]!=-1:
    e=l[e][2]

i=1
r=0
v=[0]*-~N
p=[-1]*-~N

while 1:
    n,a,b=l[i]
    if a!=-1 and v[a]<1:
        v[a]=1
        p[a]=i
        i=a
        r+=1
    elif b!=-1 and v[b]<1:
        v[b]=1
        p[b]=i
        i=b
        r+=1
    elif i==e:
        break
    else:
        i=p[i]
        r+=1

print((1<N)*r)