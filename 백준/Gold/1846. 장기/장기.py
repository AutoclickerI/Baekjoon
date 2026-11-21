n=int(input())
print(*[-1]*(n<4)or n%2*[*range(2,n-1),1,n,n-1]or[*range(3,n+1),1,2])