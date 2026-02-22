[N,M,L,K],*l=[[*map(int,i.split())]for i in open(0)]
m=0
for Y,X in l:
    t=sorted(x for y,x in l if 0<=y-Y<=L)
    p1=p2=0
    while p2<len(t):
        while p2<len(t)and t[p2]-t[p1]<=L:
            p2+=1
            m=max(m,p2-p1)
        while p2<len(t)and L<t[p2]-t[p1]:
            p1+=1
print(K-m)