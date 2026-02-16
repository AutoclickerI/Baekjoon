_,*l=[[*map(int,i.split())]for i in open(0)]
l.sort()
t=[]
c=[0]*366
for i in l:
    for j in range(i[0],i[1]+1):
        c[j]+=1
    if t and i[0]<=t[-1][1]+1:
        t[-1][1]=max(t[-1][1],i[1])
    else:
        t+=i,
r=0
for s,e in t:
    r+=(e-s+1)*max(c[s:e+1])
print(r)