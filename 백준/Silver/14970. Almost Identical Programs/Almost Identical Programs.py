while'.'!=(s:=input()):
    s=s.split('"')
    e=input().split('"')
    if s==e:
        print('IDENTICAL')
    elif s[::2]==e[::2]and sum(i!=j for i,j in zip(s[1::2],e[1::2]))==1:
        print('CLOSE')
    else:
        print('DIFFERENT')