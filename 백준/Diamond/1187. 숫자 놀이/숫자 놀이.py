n,*l=map(int,open(0).read().split())

def recur(arr,n):
    if n==2:
        a,b,c=arr
        if (a+b)%2==0:
            return a,b,c
        if (b+c)%2==0:
            return b,c,a
        return a,c,b
    else:
        use=[]
        for _ in[0]*3:
            ret=recur(arr[-n+1:],n//2)
            del arr[-n+1:]
            use+=ret[:n//2],
            arr+=ret[n//2:]
        P,Q,R=map(sum,use)
        p,q,r=use
        if (P+Q)%n==0:
            return *p,*q,*r,*arr
        if (Q+R)%n==0:
            return *q,*r,*p,*arr
        return *p,*r,*q,*arr

print(*recur(l,n)[:n])