N,M,K,*A=map(int,open(0).read().split())
A.sort()
M*=K
if sum(A)<M:print('STRESS')
else:
    r=0
    while 0<M:
        r+=1
        M-=A.pop()
    print(r)