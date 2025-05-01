C=12.01
H=1.008
N=14.01
O=16
for s in[*open(0)][1:]:print('%.3f'%eval(''.join(i+'+'*('@'<j)+'*'*('.'<j<':'<i)for i,j in zip(s,s[1:]))))