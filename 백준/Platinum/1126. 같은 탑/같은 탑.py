d={0:0}
for n in[*open(0)][1].split():
 e={**d};n=int(n)
 for k in d:e[k+n]=max(e.get(k+n,0),z:=d[k]+n);e[i]=max(e.get(i:=abs(n-k),0),z)
 d=e
print(d[0]//2or-1)