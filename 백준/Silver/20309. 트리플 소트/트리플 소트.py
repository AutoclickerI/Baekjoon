i=1
print('YNEOS'[any(int(w)&(i:=i^1)for w in[*open(0)][1].split())::2])