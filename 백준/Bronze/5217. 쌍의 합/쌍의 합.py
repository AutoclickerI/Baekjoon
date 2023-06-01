for _ in[0]*int(input()):
    n=int(input())
    print(f'Pairs for {n}: ',end='')
    l=[f'{i} {n-i}'for i in range(1,(n+1)//2)]
    print(', '.join(l))