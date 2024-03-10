(N,Q),A,*l=[map(int,i.split())for i in open(0)]
S=[x:=0]
for i in A:S+=S[-1]+i,
for i in l:
    p,q,*r=i
    if r:
        s=(q+x-1)%N
        e=(r[0]+x)%N
        if s<e:
            print(S[e]-S[s])
        else:
            print(S[-1]-S[s]+S[e])
    else:
        x+=q*(2*p-3)