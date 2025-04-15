N=int(input())

l=[input()for _ in[0]*N]

K=int(input())

lenli=[pow(10,len(i),K)for i in l]
intli=[int(i)for i in l]

state_max=2**N-1

dp=[K*[0]for _ in[0]*(state_max+1)]

dp[state_max][0]=1

from collections import deque

dq=deque([(state_max,0)])

while dq:
    state,r=dq.popleft()
    f=state
    while f:
        right=f&-f
        le=right.bit_length()-1
        nr=(r*lenli[le]+intli[le])%K
        if dp[state^right][nr]<1:
            dq+=(state^right,nr),
        dp[state^right][nr]+=dp[state][r]
        f^=right

n,d=dp[0][0],sum(dp[0])
import math
gcd=math.gcd(n,d)
print(n//gcd,d//gcd,sep='/')