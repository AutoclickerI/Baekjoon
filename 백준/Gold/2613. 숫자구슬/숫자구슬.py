N,M,*l=map(int,open(0).read().split())

def spl(m):
    ret=[0]
    t=m
    for i in l:
        if t<i:
            t=m
            ret+=0,
        t-=i
        ret[-1]+=1
    return ret

s=max(l)-1
e=30001

while 1<e-s:
    m=s+e>>1
    tr=spl(m)
    if M<len(tr):
        s=m
    else:
        e=m
        r=tr
print(e)

inv=[]
while len(r)<M:
    inv+=1,
    r[-1]-=1
    M-=1
    if r[-1]==0:r.pop()
print(*r,*inv[::-1])