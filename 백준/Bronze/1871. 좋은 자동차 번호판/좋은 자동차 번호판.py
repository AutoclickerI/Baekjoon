for z in[*open(0)][1:]:
 s=0
 i,j=z.split('-')
 for c in i:s*=26;s+=ord(c)-65
 print('not '*(100<abs(int(j)-s))+'nice')