a,b,c=map(int,input().split())
f=lambda t:(t/a/b/c%1,t/b/c%1,t/c%1)
for t in range(a*b*c):h,m,s=f(t);H,M,S=f(t+1);h>m>s!=S>=M>=H<exit(print((a*b*c-1)//-~t))