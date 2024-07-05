s,_,*l=open(0)
print(sum(all(j not in s.split()[1:]for j in i.split()[1:])for i in l))