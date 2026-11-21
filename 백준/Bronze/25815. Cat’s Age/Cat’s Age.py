p,q=map(int,input().split())
n=p*12+q
print(*divmod(9*n+[192-5*n,72,n*6][(n<13)+(n<25)],12))