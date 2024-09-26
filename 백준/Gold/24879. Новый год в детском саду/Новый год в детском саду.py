for i in[*open(0)][1:]:
    n,a,b=map(int,i.split())
    q,r=divmod(a,n)
    Q,R=divmod(b,n)
    print(n*q*Q-~r*Q-~R*q+max(0,r-n-~R))