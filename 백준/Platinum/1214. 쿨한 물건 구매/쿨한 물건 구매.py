D,P,Q=map(int,input().split())
d=min(2*P*Q+D%(P*Q),D)
a=D-d
p=0-d//-P
q=0
m=p*P
while p+1:
    if p*P+q*Q<d:
        q+=1
    else:
        m=min(m,p*P+q*Q)
        p-=1
print(a+m)