n=int(input())
print(sum(n%i<1for i in range(1,n+1,2)))