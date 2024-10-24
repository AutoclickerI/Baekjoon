for T in range(int(input())):
    p,q=input().split()
    print(end=f'Case {T+1}: ')
    t=''.join(i for i in p if i.isalpha())
    if p==q:
        print('Login successful.')
    elif p.swapcase()==q:
        print('Wrong password. Please, check your caps lock key.')
    elif t==q:
        print('Wrong password. Please, check your num lock key.')
    elif t.swapcase()==q:
        print('Wrong password. Please, check your caps lock and num lock keys.')
    else:
        print('Wrong password.')