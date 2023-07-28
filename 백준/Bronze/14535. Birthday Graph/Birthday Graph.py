i=0
while s:=int(input()):
    i+=1;l=[0]*13
    for _ in[0]*s:l[int(input()[3:5])]+=1
    print(f'Case #{i}:')
    for p,q in enumerate('Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()):print(q+':'+'*'*l[-~p])