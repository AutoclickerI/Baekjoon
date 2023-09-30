m=0
M=1260
for _ in[0]*int(input()):
    p,q,r,s=map(int,input().split())
    m=max(60*p+q,m)
    M=min(60*r+s,M)
if m<M:
    print('TAIP')
    print(m//60,m%60,M//60,M%60)
else:
    print('NE')