a=[*map(set,'123 456 789 147 258 369 159 357'.split())]
while'#'<(s:=input()):
    v,*w=s.split();v=v>'O';l=[any(i&j==i for i in a)for j in({*w[::2]},{*w[1::2]})]
    if l[0]:z='OX'[v]
    elif l[1]:z='XO'[v]
    else:z='Draw'
    print(z)