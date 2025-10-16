n,w,L,*a=map(int,open(0).read().split())

T=0
acc=0
ptr_s=0
ptr_e=0

from collections import deque

dq=deque()

while ptr_s<n:
    T+=1
    if dq and dq[0]+w<=T:
        dq.popleft()
        acc-=a[ptr_s]
        ptr_s+=1
    if ptr_e<n and acc+a[ptr_e]<=L and ptr_e-ptr_s<n:
        acc+=a[ptr_e]
        ptr_e+=1
        dq+=T,
print(T)