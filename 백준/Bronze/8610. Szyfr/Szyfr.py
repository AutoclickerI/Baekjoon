_,[s],p=open(0,'rb').read().split()
o=s-max({*p},key=p.count)
for i in p:print(end=chr((i+o+13)%26+65))