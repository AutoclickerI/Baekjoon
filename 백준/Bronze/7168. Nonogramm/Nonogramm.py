l=[input()for _ in[0]*int(input().split()[0])]
for i in l:
    p,c,*t=0,1
    i+='.'
    for j in i:
        if p=='#':
            if j=='#':c+=1
            else:t+=c,;c=1
        p=j
    print(*t or'0')
*l,=zip(*l)
for i in l:
    p,c,*t=0,1
    i+='.',
    for j in i:
        if p=='#':
            if j=='#':c+=1
            else:t+=c,;c=1
        p=j
    print(*t or'0')