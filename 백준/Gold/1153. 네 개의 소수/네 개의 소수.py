r=999999
*p,=range(r)
for i in range(2,r):
    if p[i]:p[i*i::i]=[0]*len(range(i*i,r,i))
p={*filter(int,p[2:])}
N=int(input())
if N<8:
    print(-1)
else:
    r=[2]
    N-=2
    r+=2+N%2,
    N-=2+N%2
    for i in p:
        if N-i in p:
            exit(print(*r,i,N-i))