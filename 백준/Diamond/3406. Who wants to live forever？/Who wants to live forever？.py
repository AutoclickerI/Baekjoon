for i in[*open(0)][1:]:
    n=len(i:=i.strip())+1
    if n.bit_count()==1:
        print('DIES')
    else:
        d=(n&-n)-1
        arr=[j for j in zip(*[iter(i+'0')]*-~d)]
        if len({*arr[::2]})==len({*arr[1::2]})==1 and['0',*arr[0]]==[*arr[1][::-1],'0']:
            print('DIES')
        else:
            print('LIVES')