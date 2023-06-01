try:
 while 1:
    a = int(input())
    print('TERM',a,'IS ',end='')
    b = 1
    while a > 0:
        a -= b
        b += 1
    if b % 2 == 1:
        print(f'{b + a - 1}/{1 - a}')
    else:
        print(f'{1 - a}/{b + a - 1}')
except:0