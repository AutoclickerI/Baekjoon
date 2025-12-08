for i in[*open(0)][1:]:
    n=int(i)
    d={}
    for i in range(2,n+1):
        while n%i<1:
            d[i]=d.get(i,0)+1
            n//=i
    for i in d:print(i,d[i])