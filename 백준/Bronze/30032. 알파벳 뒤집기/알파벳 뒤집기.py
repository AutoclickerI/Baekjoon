n,*l=open(0)
print(''.join(l).translate(n.maketrans('dbqp','bdpq'[::1-('1'in n[2:])*2])))