while(s:=input())!='99999':
    if s[:2]=='00':
        0
    elif sum(map(int,s[:2]))%2:
        d='left'
    else:
        d='right'
    print(d,s[2:])
    