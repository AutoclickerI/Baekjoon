for i in[*open(T:=0)][2::2]:
    T+=1
    a=''
    for s in zip(*[iter(i)]*8):a+=chr(int(''.join(s).replace('O','0').replace('I','1'),2))
    print(f'Case #{T}:',a)