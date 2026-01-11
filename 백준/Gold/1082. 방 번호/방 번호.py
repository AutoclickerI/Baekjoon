def getval(t):
    return int(''.join(map(str,t))[::-1])

N,*P,M=map(int,open(0).read().split())
l=[[0]]
for i in range(1,M+1):
    t=l[-1]
    for j in range(N):
        if P[j]<=i:
            nt=sorted(l[-P[j]]+[j])
            if getval(t)<getval(nt):
                t=nt
    l+=t,
print(getval(l[-1])//10)