S=sorted
i,*l=open(0)
print(''.join(S(sum(S(S(i)[1:]for i in l)[:int(i.split()[2])],[]))))