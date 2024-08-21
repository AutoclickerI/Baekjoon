f=lambda:map(int,input().split())
N,M=f()
for A,B in sorted(zip(f(),f())):M+=(B-A)*(A<=min(M,B))
print(M)