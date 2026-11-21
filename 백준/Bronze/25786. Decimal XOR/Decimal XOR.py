n=input()
N=input()
s=max(len(n),len(N))
n,N=int(n),int(N)
while s:
    s-=1
    T=10**s
    p,q=n//T%10,N//T%10
    print(end='90'[p<3>q or p>6<q])