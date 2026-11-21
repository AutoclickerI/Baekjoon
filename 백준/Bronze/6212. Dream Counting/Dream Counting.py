M,N=map(int,input().split())
d=[0]*10
while M<=N:
 for c in str(M):d[int(c)]+=1
 M+=1
print(*d)