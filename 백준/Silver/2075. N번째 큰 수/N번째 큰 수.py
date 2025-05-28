N=int(input())
l=[]
for _ in range(N):
    l+=map(int,input().split())
    l.sort()
    l=l[-N:]
print(l[0])