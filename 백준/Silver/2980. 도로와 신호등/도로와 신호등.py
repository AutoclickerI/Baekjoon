t=0
[N,L],*l=[[*map(int,i.split())]for i in open(0)]
i=0
for p in range(1,L+1):
    t+=1
    while i<N and l[i][0]==p and t%(l[i][1]+l[i][2])<l[i][1]:
        t+=1
    if i<N:i+=l[i][0]==p
print(t)