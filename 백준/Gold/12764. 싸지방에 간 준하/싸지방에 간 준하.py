l=[]
for _ in range(int(input())):
    l+=[[*map(int,input().split())]]
l.sort()
computer=[]
used=[]
from heapq import *
hq=[]
first=[]
cnt=0
for i in l:
    s,e=i
    while hq and hq[0][0]<s:
        _,tmp=heappop(hq)
        heappush(first, tmp)
        cnt+=1
    if cnt==0:
        computer+=[e]
        used+=[1]
        heappush(hq,(e,len(computer)-1))
    else:
        tmp=heappop(first)
        computer[tmp]=e
        used[tmp]+=1
        heappush(hq,(e,tmp))
        cnt-=1
print(len(used))
print(*used)
