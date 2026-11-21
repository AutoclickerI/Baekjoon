def f(s):
    p=n=0
    for c in s:
        if c=='P':
            p+=1
            n=0
        else:
            n+=1
    return p,n
for i in[*open(0)][1:]:
    s,e=i.split()
    s!=e
    print('YNEOS'[f(s)!=f(e)::2])