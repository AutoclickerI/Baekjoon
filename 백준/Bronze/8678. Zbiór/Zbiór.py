*l,=map(int,open(0).read().split())
[print('TNAIKE'[i%j!=0::2])for i,j in zip(l[2::2],l[1::2])]