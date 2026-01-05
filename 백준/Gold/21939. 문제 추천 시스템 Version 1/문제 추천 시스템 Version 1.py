import sys
input=sys.stdin.readline

easy=[]
hard=[]
d={}

from heapq import*
for _ in[0]*int(input()):
    P,L=map(int,input().split())
    t=[1]
    heappush(easy,(L,P,t))
    heappush(hard,(-L,-P,t))
    d[P]=t
for _ in[0]*int(input()):
    q,*l=input().split()
    if q=='add':
        P,L=map(int,l)
        t=[1]
        heappush(easy,(L,P,t))
        heappush(hard,(-L,-P,t))
        d[P]=t
    if q=='recommend':
        if l==['1']:
            while hard[0][2]==[0]:
                heappop(hard)
            P=-hard[0][1]
        else:
            while easy[0][2]==[0]:
                heappop(easy)
            P=easy[0][1]
        print(P)
    if q=='solved':
        d[int(l[0])][0]=0