for i in[*open(T:=0)][1:]:
    T+=1
    print(f'Case {T}:')
    m=min(map(i.upper().count,map(chr,range(65,91))))
    if 2<m:
        print('Triple pangram!!!')
    elif 1<m:
        print('Double pangram!!')
    elif m:
        print('Pangram!')
    else:
        print('Not a pangram')