N,Q=map(int,input().split())
*l,=map(int,input().split())
idx=-1
for _ in[0]*Q:
    q,i,*x=map(int,input().split())
    if q==1:
        l[(i+idx)%N]+=x[0]
    if q==2:
        idx-=i
    if q==3:
        idx+=i
i=(1+idx)%N
print(*l[i:]+l[:i])