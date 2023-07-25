while(s:=input())!='99999':
    if s[:2]=='00':0
    else:d=['right','left'][sum(map(int,s[:2]))%2]
    print(d,s[2:])
    