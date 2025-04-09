N,K=map(int,input().split())

def fast(N,K):
    if K==1:
        return N
    x=0
    n=1
    while n<N:
        step=max((n-x)//(1-K),n-N)
        n-=step
        x=(x-K*step)%n
    return x+1

print(fast(N,K))