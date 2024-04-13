S,K=map(int,input().split())
q,r=S//K,S%K
print(q**(K-r)*(q+1)**r)