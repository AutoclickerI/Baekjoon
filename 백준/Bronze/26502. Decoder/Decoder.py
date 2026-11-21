p,*q=open(0)
print(''.join(q).translate(p.maketrans(s:='yYaAeEiIoOuU',s[2:]+"yY")))