for s in[*open(T:=0)][1:]:
 for x in range(b:=len(s:=s[:-1])-1):s=str(int(s)+~int(v:=s[b-x:])*(v<s[b+~x]))
 T+=1;print(f'Case #{T}:',s)