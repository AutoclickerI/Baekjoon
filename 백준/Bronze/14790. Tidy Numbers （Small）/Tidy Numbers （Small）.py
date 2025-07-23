for s in[*open(T:=0)][1:]:
 s=s[:-1]
 while''.join(sorted(s))<s:s=str(int(s)-1)
 T+=1;print(f'Case #{T}:',s)