l=[*map(input().count,'UCPD')]
p,q=l[0]+l[1],l[2]+l[3]
if q>p:
    if (q+1)//2>=p:print('DP')
    else:print('UDP')
else:
    if q and p<=(q+1)//2:print('DP')
    elif q:print('UDP')
    else:print('U')