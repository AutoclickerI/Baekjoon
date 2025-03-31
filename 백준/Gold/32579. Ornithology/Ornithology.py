l=[]
for _ in[0]*int(input()):
    l+=sorted(map(int,input().split()[1:]))

cnt=[0]

def mergesort(l):
    if len(l)<2:
        return l
    n=len(l)//2
    return merge(mergesort(l[:n]),mergesort(l[n:]))

def merge(a,b):
    arr=[]
    while a and b:
        if b[-1]<a[-1]:
            cnt[0]+=len(b)
            arr+=a.pop(),
        else:
            arr+=b.pop(),
    while a:
        arr+=a.pop(),
    while b:
        arr+=b.pop(),
    return arr[::-1]

mergesort(l)

print(*cnt)