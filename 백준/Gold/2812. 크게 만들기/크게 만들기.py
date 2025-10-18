N,K=map(int,input().split())
s=input()

l=[]

for i in s:
    while l and K and l[-1]<i:
        l.pop()
        K-=1
    l+=i,
while K:
    l.pop()
    K-=1
print(*l,sep='')