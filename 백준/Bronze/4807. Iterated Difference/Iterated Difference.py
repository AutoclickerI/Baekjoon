for i in[*open(T:=0)][1::2]:
 *l,=map(int,i.split());c=0
 while c<1e3>1<len({*l}):c+=1;l=[abs(i-j)for i,j in zip(l,(2*l)[1:])]
 T+=1;print(f'Case {T}:',['not attained','%d iterations'%c][c<1000])