for i in[*open(0)][1:]:
    n,p,c,m=i.split()
    v=14+5*(p<'Q')-int(c)
    x=200+150*(p[-1]=='+')-eval(m)
    print(n,v,f'{x:.2f}','Use meal swipe or munch money'*(0<v*x)or'Use munch money'*(0<x)or'Use meal swipe'*(0<v)or'Go to Downtown Golden!')
    