for i in[*open(0)][1:]:
    n,*l=map(eval,i.split())
    f=1
    for j in range(n):
        if l[2*j]+l[2*j+1]!=n:f=0
    if f:print('no')
    else:print('yes')