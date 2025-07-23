for s in[*open(T:=0)][1:]:
 for x in range(b:=len(s:=s[:-1])-1,0,-1):s=str(int(s)+~int(v:=s[x:])*(v<s[x-1]))
 T+=1;print(f'Case #{T}:',s)