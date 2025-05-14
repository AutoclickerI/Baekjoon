for i in[*open(T:=0)][1::2]:
 l=[*map(int,i.split())];c=0
 while c<1000>1<len({*l}):c+=1;l=[abs(l[i]-l[i-1])for i in range(len(l))]
 T+=1;print(f'Case {T}:',['not attained','%d iterations'%c][c<1000])