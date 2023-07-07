l=[0,0,0,0]
for _ in[0]*int(input()):
    p,q,r=map(int,input().split())
    q-=q!=1
    l[3]+=p==1
    l[q-1]+=p!=1
print(*l)