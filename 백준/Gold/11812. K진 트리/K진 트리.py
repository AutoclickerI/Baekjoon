import sys
sys.setrecursionlimit(2*10**5)
input=sys.stdin.readline

N,K,Q=map(int,input().split())

for _ in[0]*Q:
    s,e=map(int,input().split())
    if K==1:
        print(abs(e-s))
        continue
    if e<s:
        s,e=e,s
    ds=de=0
    while (K**ds-1)//(K-1)<s:
        ds+=1
    while (K**de-1)//(K-1)<e:
        de+=1
    ans=0
    while ds<de:
        ans+=1
        de-=1
        e=0-(e-(K**de-1)//(K-1))//-K+(K**(de-1)-1)//(K-1)
    while s!=e:
        ans+=2
        de-=1
        e=0-(e-(K**de-1)//(K-1))//-K+(K**(de-1)-1)//(K-1)
        s=0-(s-(K**de-1)//(K-1))//-K+(K**(de-1)-1)//(K-1)
    print(ans)