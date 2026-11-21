p,a,b,*l=map(int,input().replace('.','').split())
for N in range(p//a+1):l+=(N,M:=(p-a*N)//b)*(a*N+b*M==p)
print(*l or['none'])