mod=2**61-1
N=int(input())
s=input()

def rh(n):
    d={}
    r=0
    for i in range(n):
        r*=128
        r+=ord(s[i])
        r%=mod
    d[r]=[0]
    p=pow(128,n-1,mod)
    for i in range(N-n):
        r-=ord(s[i])*p
        r*=128
        r+=ord(s[i+n])
        r%=mod
        d[r]=d.get(r,[])
        for j in d[r]:
            if s[i+1:i+1+n]==s[j:j+n]:
                return 1
        d[r]+=i+1,
    return 0

low=0
high=len(s)

while 1<high-low:
    m=low+high>>1
    if rh(m):
        low=m
    else:
        high=m

print(low)