M,N=map(int,input().split())
d=[0]*10
while M<=N:
 v=M
 while v:d[v%10]+=1;v//=10
 M+=1
print(*d)