p,q=map(int,input().split())
[print(*range(q*j+1,q*j+q+1))for j in range(p)]