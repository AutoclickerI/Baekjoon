N,M=map(int,input().split())
B=[1]*N
R=0
for r in map(int,input().split()):
    R+=1
    l=input().split()
    B[r-1]=-1
    for i in range(N):B[i]=min(B[i],l[i]!=l[r-1])
    if B.count(0)>B.count(1)+1:
        break
print(R)