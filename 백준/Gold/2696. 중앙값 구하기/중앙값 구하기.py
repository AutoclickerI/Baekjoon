def read(n):
    l=[]
    while len(l)<n:
        l+=map(int,input().split())
    return l

def write(l):
    while l:
        print(*l[:10])
        l=l[10:]

from heapq import*

for T in[0]*int(input()):
    l=read(int(input()))
    hqs=[]
    hql=[]
    a=[]
    for i in l:
        heappush(hql,i)
        heappush(hqs,-heappop(hql))
        if len(hql)<len(hqs):
            heappush(hql,-heappop(hqs))
        if len(hql)!=len(hqs):
            a+=hql[0],
    print(len(a))
    write(a)