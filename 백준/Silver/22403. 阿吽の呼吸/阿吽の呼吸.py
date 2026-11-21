for i in[*open(c:=0)][1:]:c=(c<0)*1e9+c+2*(i<'U')-1
print('YNEOS'[c!=0::2])