C=12010
H=1008
N=14010
O=16000
for s in[*open(0)][1:]:
    v=''
    for i,j in zip(s,s[1:]):v+=i+'+'*('@'<j)+'*'*('.'<j<':'<'@'<i)
    print(f'{eval(v)/1000:.3f}')
        