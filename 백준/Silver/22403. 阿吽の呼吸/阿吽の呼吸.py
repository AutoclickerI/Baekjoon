for i in[*open(c:=0)][1:]:
 c+=2*(i<'U')-1
 if c<0:break
print('YNEOS'[c!=0::2])