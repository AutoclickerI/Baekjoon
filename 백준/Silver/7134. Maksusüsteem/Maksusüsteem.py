[N],[*C],[*P],_,*l=[map(int,i.split())for i in open(0)]

csum=[0]
for i in C:
    csum+=csum[-1]+i,
    
csumval=[0]
for i in range(N-1):
    csumval+=csumval[-1]+P[i]*C[i],

from bisect import bisect_left
for[v]in l:
    i=bisect_left(csum,v)-1
    a=csumval[i]
    v-=csum[i]
    print('%.2f'%((a+v*P[i])/100))