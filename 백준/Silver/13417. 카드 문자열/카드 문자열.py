for i in[*open(0)][2::2]:
 s=''
 for c in i[::2]:s=min(c+s,s+c)
 print(s)