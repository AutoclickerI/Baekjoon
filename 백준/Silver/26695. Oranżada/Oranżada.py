_,k,*l=map(int,open(a:=0).read().split())
z={s:=0}
for n in l:
 if{n}&z:s+=1
 else:z|={n};a+=s;k<len(z)<exit(print(a))
print(-1)