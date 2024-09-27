_,s,p=open(0,'rb').read().split()
o=s[0]-max({*p},key=p.count)
print(''.join(chr((i+o+13)%26+65)for i in p))