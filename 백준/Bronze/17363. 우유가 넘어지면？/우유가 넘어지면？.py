_,*l=open(0)
for i in[*zip(*[s.translate(str.maketrans('-|/\^<v>','|-\/<v>^'))[:-1]for s in l])][::-1]:print(*i,sep='')