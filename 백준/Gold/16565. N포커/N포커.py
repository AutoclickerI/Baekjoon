N=int(input())

dp={}

# from n cards, choose c card with no 4 of a kind
def f(n,c):
    if n<=c or c<0:
        return 0
    if(n,c)not in dp:
        if n==4:
            dp[n,c]=math.comb(4,c)
        else:
            dp[n,c]=(f(n-4,c)+f(n-4,c-1)*4+f(n-4,c-2)*6+f(n-4,c-3)*4)%10007
    return dp[n,c]

import math

print((math.comb(52,N)-f(52,N))%10007)