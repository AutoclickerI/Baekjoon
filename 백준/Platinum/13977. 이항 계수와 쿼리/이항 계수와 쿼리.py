import sys
P=10**9+7
d={0:1}
for i in range(1,4*10**6+1):d[i]=d[i-1]*i%P
def m(x,n):
 return x if n==1 else m(x,n//2)**2%P if n%2==0 else m(x,n//2)**2*x%P
for i in[0]*int(input()):n,k=map(int,sys.stdin.readline().split());print(d[n]*m(d[k]*d[n-k],P-2)%P)