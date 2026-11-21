_,k,*l=map(int,open(0).read().split())
a=s=0
z={0}
for n in l:
 if n in z:s+=1
 else:z|={n};a+=s;k<len(z)<exit(print(a))
print(-1)