x,k,a=map(int,input().split())
i=0
while x>=0:
    x-=[k,a][i]
    i^=1
print(i)