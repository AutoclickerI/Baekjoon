_,[s],p=open(0,'rb').read().split()
o=s-max({*p},key=p.count)
print(''.join(chr((i+o+13)%26+65)for i in p))