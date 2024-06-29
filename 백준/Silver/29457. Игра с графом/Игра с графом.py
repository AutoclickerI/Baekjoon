n,m=map(int,input().split())
print([['Bob','Alice'][n-m&1],'Draw'][n<2])