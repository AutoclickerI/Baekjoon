for s in[*open(T:=0)][1:]:
 s=int(s)
 while int(''.join(sorted(str(s))))-s:s-=1
 T+=1;print(f'Case #{T}:',s)