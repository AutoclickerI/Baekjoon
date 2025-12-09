T=0
for i in[*open(0)][:-1]:
    T+=1
    r=p=0
    for c in i[:-1]:
        if c=='{':
            p+=1
        else:
            p-=1
        if p<0:
            p+=2
            r+=1
    print(f'{T}.',r+p//2)