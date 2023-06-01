n,l,m,r=map(int,input().split())
M=10**9+7
R=pow(l+m+r,-1,M)
N=l-r
def f(a,n):
 if n==0:return(1,0),(0,0),(0,0)
 if n%2:[p,P],[q,Q],[r,R]=f(a,n-1);return((a[0]*p-a[1]*P)%M,(a[0]*P+a[1]*p)%M),((p+q)%M,(P+Q)%M),((r+(n-1)*p)%M,(R+(n-1)*P)%M)
 [p,P],[q,Q],[r,R]=f(a,n//2);return((p*p-P*P)%M,2*p*P%M),((q*(1+p)-P*Q)%M,((1+p)*Q+q*P)%M),((r*(1+p)-R*P+n//2*(p*q-P*Q))%M,(R*(1+p)+r*P+n//2*(P*q+p*Q))%M)
p,q,r=f((m*R,N*R),n)
s,t,u=f((m*R,-N*R),n)
print(((q[0]+t[0])*n-r[0]-u[0]-n)%M)