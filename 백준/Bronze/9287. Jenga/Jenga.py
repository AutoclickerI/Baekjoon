for T in range(1,int(input())+1):
    l=[input()in'10001'for _ in[0]*int(input())]
    print(f'Case {T}:',['Standing','Fallen'][any(l)])