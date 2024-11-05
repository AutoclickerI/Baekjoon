import sys
input=sys.stdin.readline

import math
a,d=map(int,input().split())
for _ in[0]*int(input()):
    q,l,r=map(int,input().split())
    if q==1:
        print((a+d*(l-1)+a+d*(r-1))*(r-l+1)//2)
    else:
        if d==0:
            print(a)
        else:
            ans=a+d*(l-1)
            for i in range(d*l,d*r,d):
                ans=math.gcd(ans,a+i)
                if ans<2:
                    break
            print(ans)