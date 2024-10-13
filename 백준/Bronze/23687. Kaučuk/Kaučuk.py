a=b=c=0
for i in[*open(0)][1:]:
    t,s=i.split()
    if t == 'section':
        a, b, c = a + 1, 0, 0
        print(a, s)
    elif t == 'subsection':
        b += 1
        print(f'{a}.{b}', s)
    else:
        c += 1
        print(f'{a}.{b}.{c}', s)