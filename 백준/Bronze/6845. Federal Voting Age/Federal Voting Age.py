p,q,r=2007,2,27
for _ in[0]*int(input()):
    P,Q,R=map(int,input().split())
    if p-P>18:print('Yes')
    elif p-P==18:
        if q>Q:print('Yes')
        elif q==Q and r>=R:print('Yes')
        else:print('No')
    else:print('No')