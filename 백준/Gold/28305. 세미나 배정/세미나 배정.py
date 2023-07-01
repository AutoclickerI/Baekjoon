from heapq import*
N,T=map(int,input().split())
l=sorted(map(int,input().split()))
def possible(n):
    seminar=[0]*n
    for i in range(N):
        if l[i]<=seminar[i%n]:
            return 0
        seminar[i%n]=max(seminar[i%n]+T,l[i])
    return 1
s=0
e=N
while e-s>1:
    m=(s+e)//2
    if possible(m):e=m
    else:s=m
print(e)