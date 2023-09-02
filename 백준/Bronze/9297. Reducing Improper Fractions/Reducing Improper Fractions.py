for i in range(int(input())):
    p,q=map(int,input().split())
    if p%q:
        if p//q:
            print(f'Case {i+1}: {p//q} {p%q}/{q}')
        else:
            print(f'Case {i+1}: {p%q}/{q}')
    else:
        if p//q:
            print(f'Case {i+1}: {p//q}')
        else:
            print(f'Case {i+1}: 0')