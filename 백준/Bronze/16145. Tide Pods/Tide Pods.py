ans=[]
t_=n_=0
for _ in range(int(input())):
    if t_==n_==0:t,n=map(int,input().split())
    else:t,n=t_,n_
    t_,n_=0,0
    li=eval('[*map(int,input().split())],'*n)
    *k,=map(int,input().split())
    if len(k)>t:*k,t_,n_=k
    tt=[]
    for i in li:
        *i,b=i;c=0
        for p,q in zip(k,i):c+=p==q==1
        tt.append(c*b)
    ans+=f"Data Set {_+1}:",abs(max(tt)-min(tt)),""
print(*ans,sep='\n')