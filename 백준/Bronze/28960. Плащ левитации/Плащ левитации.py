H,L,A,B=map(int,input().split())
A,B=sorted([A,B])
if B<=L:
    if A<=2*H:
        print('YES')
    else:
        print('NO')
elif A<=L:
    if B<=2*H:
        print('YES')
    else:
        print('NO')
else:
    print('NO')