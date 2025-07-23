for s in[*open(T:=0)][1:]:
 b=len(s:=s[:-1])-1;T+=1
 for x in range(b):s=str(int(s)+~int(v:=s[b-x:])*(v<s[b+~x]))
 print(f'Case #{T}:',s)