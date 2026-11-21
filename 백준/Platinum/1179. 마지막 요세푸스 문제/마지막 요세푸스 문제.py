N,K=map(int,input().split())

if K==1:exit(print(N))
x=0
n=1
while n<N:
    step=max((n-x)//(1-K),n-N)
    n-=step
    x=(x-K*step)%n
print(x+1)