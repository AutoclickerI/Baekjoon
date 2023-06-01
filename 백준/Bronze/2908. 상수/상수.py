a = input().split()
b, c = f'{a[0][2]}{a[0][1]}{a[0][0]}', f'{a[1][2]}{a[1][1]}{a[1][0]}'
if int(b) > int(c):
    print(b)
else:
    print(c)