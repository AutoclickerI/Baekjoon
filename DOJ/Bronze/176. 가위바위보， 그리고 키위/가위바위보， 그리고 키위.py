A=input()
B=input()
if A=='K':
    print('S')
elif B=='K':
    print('M')
elif A+B in'SPRS':
    print('M')
else:
    print('S')