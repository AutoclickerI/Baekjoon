N,K=map(int,input().split())

def naive(N,K):
    r=0
    
    i=N
    while i:
        r+=K%i
        i-=1
    
    return r

def fast(N,K):
    r=0
    
    if N>K:
        r=K*(N-K)
        N=K
    
    i=N
    while 1<i:
        if K%i<K%(i-1) and K//i==K//(i-1):
            step=K%(i-1)-K%i
            p=0-(K%i-i)//(step+1)
            r+=(K%i*2+(p-1)*step)*p//2
            i-=p
        else:
            r+=K%i
            i-=1
    
    return r

print(fast(N,K))