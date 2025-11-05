[N],*l=[[*map(int,i.split())]for i in open(0)]
l.sort()
from heapq import*
hq=[]
a=0
while N:
   while l and N<=l[-1][0]:
       t,c=l.pop()
       heappush(hq,-c)
   if hq:a-=heappop(hq)
   N-=1
print(a)