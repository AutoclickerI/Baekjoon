N,M=map(int,input().split())
c=N==M
print((min(N,M)+~c)**2+c)