(n,q),[*r],*z=[map(int,i.split())for i in open(0)]
d=r.index(0)

t=set()
u=[set()for _ in[0]*n]

for i in range(q):
    c,a,*l=z[i]
    a-=1
    if c==1:
        b=l[0]-1
        
        if r[a]==0:
            u[b]|={i}
        elif r[a]==1:
            u[b]|={i}
            if r[b]==2:u[d]|={i}
        else:
            if r[b]==1:t|={i};u[d]|={i}
            else:u[b]|={i}

    elif c==2:
        x=l[0]-1
        
        if r[a]==1 and x in t:t-={x}
        else:u[a]-={x}

    else:print(len(u[a])+len(t)*(r[a]==1))