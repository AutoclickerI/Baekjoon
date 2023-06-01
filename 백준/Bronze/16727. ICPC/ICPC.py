a,b=map(int,input().split())
c,d=map(int,input().split())
if a+d>c+b:
    print('Persepolis')
elif a+d<c+b:
    print('Esteghlal')
else:
    if b>d:
        print('Esteghlal')
    elif b<d:
        print('Persepolis')
    else:
        print('Penalty')
    