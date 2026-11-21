[N,*_],S,*l=[[*map(int,i.split())]for i in open(0)]
S={*S}
l.sort()
for i in range(N):
    a=[0]*N
    a[i]=1
    for _,s,e in l:a[e-1]|=a[s-1]
    {i+1 for i in range(N)if a[i]}==S!=print(i+1)