for T in range(1,int(input())+1):
    l=[input()for _ in[0]*int(input())]
    print(f'Case #{T}:',min(l,key=lambda s:(-len({*s}-{' '}),s)))