print(n:=int(input()))
while n-1:
    if n%2:n=3*n+1
    else:n//=2
    print(n)