s='1110111','0010010','1011101','1011011','0111010','1101011','1101111','1010010','1111111','1111010'
a,b,c,d,e,f=[[j for j in range(10)if all(q in[p,'-']for p,q in zip(s[j],i[::2]))]for i in open(0)]

for i in a:
    for j in b:
        for k in c:
            for l in d:
                for m in e:
                    for n in f:
                        if 10*i+j<24 and 10*k+l<60 and 10*m+n<60:
                            print(f'{10*i+j:02}:{10*k+l:02}:{10*m+n:02}')