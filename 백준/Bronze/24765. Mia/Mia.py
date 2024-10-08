while'1'<(p:=input()):
    s0,_,s1,_,r0,_,r1=p
    a=max(s0,s1)+min(s0,s1)
    b=max(r0,r1)+min(r0,r1)
    if a=='21':v=+(b!='21')
    elif b=='21':v=2
    elif s0==s1:
        if r0==r1:v=(a>b)+(a<b)*2
        else:v=1
    elif r0==r1:v=2
    else:v=(a>b)+(a<b)*2
    if v:print('Player',v,'wins.')
    else:print('Tie.')