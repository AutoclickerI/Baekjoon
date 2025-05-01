C=12010
H=1008
N=14010
O=16000
for s in[*open(0)][1:]:
    v=''
    for i,j in zip(s,s[1:]):
        v+=i
        if j.isalpha():
            v+='+'
        if i.isalpha()and j.isdigit():
            v+='*'
    print(f'{eval(v)/1000:.3f}')
        