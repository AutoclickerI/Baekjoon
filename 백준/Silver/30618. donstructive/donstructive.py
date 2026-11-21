n=int(input())
print(*range(1,n+1,2),*range(n&~1,0,-2))