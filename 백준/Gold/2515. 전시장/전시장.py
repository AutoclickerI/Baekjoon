[N,S],*l=[[*map(int,i.split())]for i in open(0)]
l.sort()
v=[0]*N
m=p=0
for i,(H,C)in enumerate(l):
    while l[p][0]+S<=H:
        m=max(m,v[p])
        p+=1
    v[i]=m+C
print(max(v))