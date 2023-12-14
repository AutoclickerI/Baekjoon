l,r=map(input().count,'LR')
n=int(input())
if l and r:
    print('YES')
elif l:
    if l<=-n:
        print('YES')
    else:
        print('NO')
else:
    if r<=n:
        print('YES')
    else:
        print('NO')