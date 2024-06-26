for T in range(int(input())):
    *b,=input()+input()+input()
    s=input()
    for i in range(9):
        if b[i]<'o':
            b[i]=s
            if[s,s,s]in[b[:3],b[3:6],b[6:],b[2:8:2],b[::4],b[::3],b[1::3],b[2::3]]:
                print(f'Case {T+1}:',*map(''.join,[b[:3],b[3:6],b[6:]]),sep='\n')
            b[i]='-'