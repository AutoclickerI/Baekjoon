for _ in[0]*int(input()):
    s=input()
    p,q,r,P,Q,R=map(int,s.split())
    f=p+q+r>P+Q+R
    F=p>P or p==P and q>Q or p-P==q-Q==0 and r>R
    print(s)
    if f+F==2:
        print('both\n')
    elif f:
        print('count\n')
    elif F:
        print('color\n')
    else:
        print('none\n')