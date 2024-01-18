m=1e18
M=-m
for i in[*open(0)][1:]:
    p,q=map(int,i.split(':'))
    t=p*60+q
    if 389<t<1141:
        m=min(m,t)
        M=max(M,t)
a=0
if 389<m<601:
    if 389<M<961:
        a=24000
    if 960<M<1141:
        a=36000
if 600<m<961 and 600<M<961:
    a=16800
if 600<m<1141 and 960<M<1141:
    a=24000
print(a)