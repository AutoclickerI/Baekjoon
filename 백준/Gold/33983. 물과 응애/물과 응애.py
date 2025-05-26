from heapq import*

try:
    N=int(input())
    s=input()
    hq_l=[]
    hq_r=[]
    for i in range(N):
        if s[i]=='H':
            heappush(hq_r,i)
    for i in range(N):
        if s[i]=='O':
            while hq_r[0]<i:
                heappush(hq_l,heappop(hq_r))
            heappop(hq_l)
    while hq_l:
        heappush(hq_r,heappop(hq_l))
    for i in range(N):
        if s[i]=='O':
            assert i<heappop(hq_r)
    assert hq_l==hq_r==[]
    print('pure')
except:
    print('mix')