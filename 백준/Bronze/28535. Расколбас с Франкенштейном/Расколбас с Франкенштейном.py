a,b,c=input().split()
if 'R'in a+c:
    print('R')
elif a==c=='N'and b in'+*':
    print('N')
elif b=='/'or'Q'in a+c:
    print('Q')
else:
    print('Z')