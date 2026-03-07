mod=10**9+7

def maxD(d):
    if d<0:
        r=1
        for a,b in l:
            r=r*max(min(d,b)-a+1,0)%mod
        return r
    v=[0]*-~d
    v[0]=1
    for a,b in l:
        s=[0]
        for i in v:
            s+=s[-1]+i,
        t=[0]*-~d
        for j in range(d+1):
            t[0]+=v[j]*max(min(b,-j)-a+1,0)
        t[0]%=mod

        for k in range(1,d+1):
            L=max(0,k-b)
            R=min(d,k-a)
            if L<=R:
                t[k]=(s[R+1]-s[L])%mod
        v=t
    return sum(v)

for T in[0]*int(input()):
    N,D=map(int,input().split())
    l=[[*map(int,input().split())]for _ in[0]*N]
    print((maxD(D)-maxD(D-1))%mod)