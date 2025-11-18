for i in[*open(0)][1:]:
    N,K=map(int,i.split())
    if N==1:print(K)
    else:
        r,q=divmod(K,2*N-2);b=[r]+[2*r]*(N-2)+[r];d=i=0
        while q:b[i]+=1;d^=i in[0,N-1];i+=2*d-1;q-=1
        print(*b)