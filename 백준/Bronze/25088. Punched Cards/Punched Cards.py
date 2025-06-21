for T in range(1,int(input())+1):
    R,C=map(int,input().split())
    print(f'Case #{T}:')
    print('..+'+'-+'*~-C)
    print('.'+'.|'*C)
    print('+'+'-+'*C)
    for _ in[0]*~-R:
        print('|'+'.|'*C)
        print('+'+'-+'*C)