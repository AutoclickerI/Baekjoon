f=8
for i in[*open(0)][1].split():
    a=f&1;b=(f&2)>>1;c=(f&4)>>2;d=(f&8)>>3
    p=a*8+d*4+c*2|b*2;q=c*8+d*4+b|a
    if'1'==i:f=p
    if'0'==i:f=q
    if'-1'==i:f=p|q
for i in f'{f:04b}':print('JEAIH'[i=='0'::2])