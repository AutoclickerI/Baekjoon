N,C,*l=map(int,open(0).read().split())

def getlist(arr):
    z=[]
    for i in range(2**len(arr)):
        n=0
        for v in arr:
            if i%2:
                n+=v
            i//=2
        z+=n,
    return sorted(z)

left,right=getlist(l[:N//2]),getlist(l[N//2:])

ans=0

from bisect import*

for i in left:
    ans+=bisect(right,C-i)
print(ans)