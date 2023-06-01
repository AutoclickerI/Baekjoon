j=0
for i in[*open(0)][1:]:_,a,b,c,d=map(int,i.split());j+=1;print(f'Case {j}:','NYOE S'[(abs(c-a),abs(d-b))in[(1,2),(2,1)]::2])